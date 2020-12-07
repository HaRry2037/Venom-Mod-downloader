#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import random 
import os
from colorama import Fore

os.system('clear')

w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
c = Fore.CYAN
y = Fore.YELLOW

colors = (w, g, r, b, c, y)
color = random.choice(colors)

banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ███╗   ███╗ ██████╗ ██████╗       ███████╗███████╗████████╗ ██████╗██╗  ██╗███████╗██████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ████╗ ████║██╔═══██╗██╔══██╗      ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██╔████╔██║██║   ██║██║  ██║█████╗█████╗  █████╗     ██║   ██║     ███████║█████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║╚██╔╝██║██║   ██║██║  ██║╚════╝██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║ ╚═╝ ██║╚██████╔╝██████╔╝      ██║     ███████╗   ██║   ╚██████╗██║  ██║███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝     ╚═╝ ╚═════╝ ╚═════╝       ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

     [+] Created By Venom
     [+] Instagram - i.m.gauravchaudhary
     [+] Whatsapp - +91 9910332273


'''
print(color + banner + color)
links = []
heading = []
app_link = []
final_link = []
down_apk = input(w + '    [+] '+ w + color + 'Enter the apk you want to find mod of: ' + color) 
url = 'https://moddroid.com/?s=' + down_apk
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
x = 0
for i in soup.find_all('a', class_="d-flex position-relative archive-post"):
     title = i.get('title')
     link = i.get('href')
     links.append(link)
     heading.append(title)
for i in heading:
    print(w + '    [' + str(x) + '] ' + w + g + i + g)
    x += 1
print(' ')
count = int(input(w + '    [+] ' + w + color + 'Select the apk you want to download: ' + color))
apk_link = links[count]
_response = requests.get(apk_link)
_soup = BeautifulSoup(_response.content, 'html.parser')
new_link = _soup.find('a' , class_='btn btn-secondary btn-block mb-3')
_new_link = new_link.get('href')
#3
down = requests.get(_new_link)
_down = BeautifulSoup(down.content, 'html.parser')
for apk in _down.find_all('a', class_='btn btn-secondary px-5'):
    _apk = apk.get('href')
    app_link.append(_apk)
final = requests.get(app_link[0])
_final = BeautifulSoup(final.content, 'html.parser')
for i in _final.find_all('a', class_='btn btn-secondary px-5'):
    venom = i.get('href')
    if venom.startswith('https://files.moddroid.com/') is True:
        final_link.append(venom)
    elif venom.startswith('https://apple.spiderdown.com') is True:
        final_link.append(venom)
    else:
        pass
downloaded = os.system('wget ' + final_link[0])
print(downloaded)

