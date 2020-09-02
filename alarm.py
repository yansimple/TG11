import telebot
import datetime
import time
token = "878636076:AAG9tG9Lyx2l1Lncdpl0Y2cFTwluQ28qonk"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def alarm(message):
	if message.chat.id != 1:
		while True:
			now = datetime.datetime.now()
			time_check = now.strftime("%H%M%S")
			print(time_check)
			if str(time_check) == "230000":
				bot.send_message(message.chat.id, "!ВЫПЕЙ КВЕТИАПИН!")
				time.sleep(1)
				continue

			else:
				time.sleep(1)
				continue
	print("Out of loop!")
	message
		

bot.polling(none_stop=True)