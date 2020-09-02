import requests
import telebot

tgtoken = "400971236:AAH8jDwygQ0VxxJjPy6gE6J0RDrj5FDBZv4"

bot = telebot.TeleBot(tgtoken)

ABC_list =('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')

@bot.message_handler(commands=['start', 'help'])

def start_info(massage):
    info_text = """Приветсвуем! Это бот-переводчик от @yansimple Присылайте ему текст или слово на русском/английском и получите мгновенный перевод. V2.04"""
    print("| User ID: ", massage.chat.id, " start")
    bot.send_message(massage.chat.id, info_text)

@bot.message_handler(content_types=["text"])
def trans_read(massage):
    input_user = massage.text

    eng_text = input_user

    token = "trnsl.1.1.20181225T164207Z.d387221d99499e03.6560c4f87dcde022b22f89b71e36db58d709bac8"

    id = massage.chat.id
    id = str(id)
    def add_DATABASE():
        db = open("DataBaseId.txt", "r")
        List_Id = db.read()
        List_Id = List_Id.split(",")
        db.close()
        id_in_list = id
        if id_in_list not in List_Id:
            db = open("DataBaseId.txt", "a")
            string_add = (str(id)+",")
            db.write(string_add)
            print(id, " was added")
            db.close()
            input()
        else:
            print("ID "+id+" allready in DataBase")

    add_DATABASE()

    if input_user[0] in ABC_list:
        url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
        webRequest = requests.get(url_trans, params = trans_option)
        rus_text = webRequest.text
        rus_text = rus_text[36:(len(rus_text)-3)]
        print(eng_text," → ", rus_text,"| User ID: ", massage.chat.id)
        bot.send_message(massage.chat.id, rus_text)

    else:
        url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        trans_option = {'key':token, 'lang':'ru-en', 'text': eng_text}
        webRequest = requests.get(url_trans, params = trans_option)
        rus_text = webRequest.text
        rus_text = rus_text[36:(len(rus_text)-3)]
        print(eng_text," → ", rus_text,"| User ID: ", massage.chat.id)
        bot.send_message(massage.chat.id, rus_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
