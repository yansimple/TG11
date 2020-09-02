from urllib.request import urlopen
import json
import telebot
import time
import datetime
import copy
now = datetime.datetime.now()
time_check = now.strftime("%d-%m-%Y %H:%M:%S")
token = "880113181:AAH7gjTlSprxkVjavHT-lvHb5tnwV1ioLO8"
bot = telebot.TeleBot(token)
 # welcome message
@bot.message_handler(command=['start','help'])

def start(massage):
    info_text = "Отправтье свой Bitcoin-адресс боту, чтобы получить оповещение при наличии 2х подтверждений и текущего колличества подтверждений.\nDev by @yansimple"
    print("| User ID: ", massage.chat.id, " start")
    bot.send_message(massage.chat.id, info_text)

#get link
@bot.message_handler(content_types=["text"])
def tx_notif(massage):
    try:
        wallet = massage.text
        url = 'https://blockchain.info/rawaddr/' + wallet
        response = urlopen(url)
        url1 = "https://blockchain.info/q/getblockcount"
        response1 = urlopen(url1)
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        string1 = response1.read().decode('utf-8')
        all_blocks = json.loads(string1)
        tx_id = json_obj['txs'][0]['inputs'][0]["prev_out"]['spending_outpoints'][0]['tx_index']
        set_tx = copy.copy(tx_id) #Привязка к заданной транзакции
        link_tx = "https://blockchain.info/rawtx/" + str(set_tx)        	
        response_tr = urlopen(link_tx)
        string_tr = response_tr.read().decode('utf-8')
        height_json = json.loads(string_tr)
        mes1 = "Адрес '"+str(wallet)+"' получен успешно, последняя транзакция отслежена, ID транзакции - "+str(set_tx)+"\nОжидайте уведомления!"
        bot.send_message(massage.chat.id, mes1)
        #Старт цикла с выбранной транзакцией
        while True:
            now = datetime.datetime.now()
            time_check = now.strftime("%d-%m-%Y %H:%M:%S")

            url = 'https://blockchain.info/rawaddr/' + wallet
            response = urlopen(url)
            url1 = "https://blockchain.info/q/getblockcount"
            response1 = urlopen(url1)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            string1 = response1.read().decode('utf-8')
            all_blocks = json.loads(string1)
            tx_id = json_obj['txs'][0]['inputs'][0]["prev_out"]['spending_outpoints'][0]['tx_index']
            set_tx = copy.copy(tx_id) #Привязка к заданной транзакции
            link_tx = "https://blockchain.info/rawtx/" + str(set_tx)
                
            response_tr = urlopen(link_tx)
            string_tr = response_tr.read().decode('utf-8')
            height_json = json.loads(string_tr)
            try:
                height = height_json["block_height"]
                number_conf = all_blocks - height + 1
                print("check TX", number_conf)
                if number_conf >= 2:
                    print("NOTIFICATION! ", massage.chat.id)
                    print(number_conf)
                    mes_notif = "Получено "+str(number_conf)+" подтверждения на транзакции "+str(set_tx)+"\nserver time "+str(time_check)+"\nВаш кошелек '"+str(wallet)+"'\nЕсть вопросы? Напишите @yansimple"
                    bot.send_message(massage.chat.id, mes_notif)
                    break
                else:
                    print(number_conf, set_tx, wallet, massage.chat.id)
                    print("sleeping now 5 sec", time_check)
                    time.sleep(5)
                    continue
            except KeyError:
                print("No conformation on TX", " ", tx_id)
                mes3 = "На на кошельке '" + str(wallet) + " Имеется неподтвержденная транзакция, id транзакции\n"+ str(set_tx)
                #bot.send_message(massage.chat.id, mes3)
                print("sleeping now 5 sec", time_check)
                time.sleep(5)
                continue
        print("End check")
    except:
        print("error")
        bot.send_message(massage.chat.id, "Oops! Something went wrong, check the address of your wallet and try again!")

bot.polling(none_stop=True)
