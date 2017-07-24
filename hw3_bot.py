#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import re
import pyautogui as gui
import pyperclip
import time

list_url = 'https://docs.google.com/spreadsheets/d/1xZ4bVdKiDei-6mzauqo-bvoDtns53U2RlfTwwGpgxk0/pubhtml'

soup = bs(requests.get(list_url).text, 'html.parser')
each_person = soup.find_all('tr')
next = 0

for idx, person in enumerate(each_person):
    td = person.find_all('td')
    if len(td) == 0:
        continue
    print(td[3].contents)
    if not re.search('</a>', str(td[3].contents)):
        continue
    if person.a.contents[0][0:5] == 'http:':
        url = 'https://ideone.com/plain' + person.a.contents[0][17:]
    else:
        url = 'https://ideone.com/plain' + person.a.contents[0][18:]
    #for t in td:
    #    print(t)
    name = td[1].contents[0]
    id = td[2].contents[0]
    comment = td[4].contents
    print('\n\n==========')
    print(idx-1)
    print(name)
    print(id)
    print(comment)
    #print(url)
    print()

    code = requests.get(url).text
    #print(code)
    try:
        # open chrome
        gui.hotkey('win','r')
        time.sleep(0.2)
        gui.typewrite('chrome')
        gui.press('enter')
        time.sleep(0.2)
        gui.hotkey('win', 'up')
        time.sleep(0.2)
        gui.hotkey('ctrl', 't')
        time.sleep(0.2)
        gui.typewrite('https://goo.gl/forms/DwyOosJFhy4afunf1')
        gui.press('enter')
        time.sleep(2)

        # type name
        print(name)
        pyperclip.copy(name)
        loc = gui.locateOnScreen('name.png')
        center = gui.center(loc)
        gui.click(center)
        gui.hotkey('ctrl', 'v')

        exec(code)

        #close chrome
        gui.hotkey('ctrl', 'w')
        time.sleep(0.2)
        gui.hotkey('ctrl', 'w')
        time.sleep(0.2)
    except:
        print('===== Bad Code =====')
        print(code)
        continue
