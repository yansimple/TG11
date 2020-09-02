import telebot
tgtoken = "400971236:AAH8jDwygQ0VxxJjPy6gE6J0RDrj5FDBZv4"
bot = telebot.TeleBot(tgtoken)
db = open("DataBaseId.txt", "r")
list_id = db.read()
list_id_splited = list_id.split(",")
print(list_id_splited)
for id in list_id_splited:
    print("send to")
    Post_text = "Добро пожаловать в помойку интернета! Это не DarkNet, это как минимум DirtyNet! t.me/DunkyYan "
    def send_post():
        bot.send_message(id, Post_text)
        print("was send '"+id+"'")
        time.sleep(1)
    try:
        send_post()
    except:
        print("\nUser id '"+id+"' stop use Bot\n")
        continue
