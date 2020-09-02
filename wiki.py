import wikipedia
import telebot

wikipedia.set_lang("RU")
token = "826471649:AAHERZVLHzOk2IqJ3j6nH3Hjk9zTfgq9tEw"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])

def wiki(massage):
    try:
        user_req = massage.text

        print(massage.chat.id)

        page = wikipedia.page(user_req)
        send_wiki = str(wikipedia.summary(user_req)) + "\n" + page.url
        bot.send_message(massage.chat.id, send_wiki)
    except:
        bot.send_message(massage.chat.id, "Множество вариантов ответов, будте конкретнее!")
if __name__ == '__main__':
    bot.polling(none_stop=True)
#wiki_req = input("введите запрос: ")
#rint(str(wikipedia.summary(wiki_req)))
