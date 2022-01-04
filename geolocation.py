import requests
import json
import os



import geocoder
g = geocoder.ip('me')   #показывает город
geo_in_json = json.dumps(g.geojson, indent=4, sort_keys=True)
print(geo_in_json)

'''
---------------------------------------------------------------
# вариант 1 - не точный , показывает львов!
---------------------------------------------------------------
# send_url = "http://api.ipstack.com/check?access_key=07941b90313d900fbce0d8f3a64fb62f"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# print(geo_json)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']
# print(city, latitude, longitude)


---------------------------------------------------------------
# вариант 2 - заебись охуенно!
---------------------------------------------------------------
data = os.system('curl ipinfo.io')
print(data)
'''


# глянуть функцию этого чела
# def Phoneseaker():
# import urllib.request
# import json
# phone = input("Enter phone: ")
# getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
# try:
# infoPhone = requests.get( getInfo )
# except:
# print( "\n[!] - Phone not found - [!]\n" )
# infoPhone = infoPhone.json()
# print( u"Номер сотового --->", "+" + phone )
# print( u"Страна ---> ", infoPhone["fullname"] )
# print("Город ---> ", infoPhone["capital"]["name"])
# print("Широта и долгота ---> ", infoPhone["capital"]["latitude"], infoPhone["capital"]["longitude"])
# print( u"Оператор ---> ", infoPhone["0"]["oper"] )
# print( u"Часть света ---> ", infoPhone["country"]["location"] )

