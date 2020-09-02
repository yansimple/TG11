import requests
import telebot
from telebot import types
import json

tgToken = "579444269:AAEXK0dRTtXtc5vzh7R-GC5NviwleW0v9c0"

bot = telebot.TeleBot(tgToken)


@bot.message_handler(command="start")
def start(massage):
    info_text = "Это бот от @yansimple , который показывает погоду, просто отправьте ему геопозицию!"
    print("| User ID: ", massage.chat.id, " start")
    bot.send_message(massage.chat.id, info_text)


@bot.message_handler(content_types=["location"])
def set_loc(massage):
    user_loc = massage.location
    Location = str(user_loc)
    lon = Location[14:21]
    lat = Location[37:44]
    print(Location)
    print(lon, lat)

    URL = ("http://api.openweathermap.org/data/2.5/forecast?lat=" +
           lat + "&lon=" + lon + "&APPID=8ce732d6a12e718cc51c41b47b7242cb")
    webRequest = requests.get(URL)
    answer = webRequest.text
    json_string = answer

    temp = json.loads(json_string)
    try:
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
            else:
                print("ID "+id+" allready in DataBase")

        add_DATABASE()

        list = temp["list"]
        dict = list[1]
        dict2 = dict['main']
        temp_k = dict2['temp']
        temp = (temp_k - 273.15)
        temp = round(temp, 1)
        temp_min = dict2["temp_min"]
        temp_min = (temp_min - 273.15)
        temp_min = round(temp_min, 1)
        temp_max = dict2["temp_max"]
        temp_max = (temp_max - 273.15)
        temp_max = round(temp_max, 1)

        cl = json.loads(json_string)
        clouds = cl["list"][12]
        clouds = clouds["clouds"]
        cloud_weather = clouds["all"]
        # \nМакс. температура сегодня: " + str(temp_max) + "°C\nМин. температура сегодня: " + str(temp_min) + "°C"
        weather_text = "Температура в настоящее время: " + \
            str(temp) + "°C\nОблачность: " + str(cloud_weather) + "%\n{Open Testing}\n By @yansimple"
        bot.send_message(massage.chat.id, weather_text)
        print(weather_text)
    except:
        print("\n\n\nLocation error\n\n\n")
        bot.send_message(massage.chat.id, "Погода в данном регионе сейчас не доступна, по всем вопросам обращайтесь к @yansimple")


if __name__ == '__main__':
    bot.polling(none_stop=True)
