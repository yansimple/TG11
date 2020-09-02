import json, requests
URL =("http://api.openweathermap.org/data/2.5/forecast?lat=" +
         "60.000000" + "&lon=" + "30.600000" + "&APPID=8ce732d6a12e718cc51c41b47b7242cb")
webRequest = requests.get(URL)
answer = webRequest.text
json_string = answer

temp = json.loads(json_string)
print(temp)
print(temp["list"]["weather"]['wind']['speed'])
