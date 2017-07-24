import requests
from bs4 import BeautifulSoup as bs
import pyautogui as gui
import time

list_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ_b_AUfJ_3_wk0ZPAB5HItzE1LqTjecO7ADWVSalhBwOyXG5fvL83XnMDg2TE_RxPbKdDbgyNJJKKS/pubhtml'

soup = bs(requests.get(list_url).text, 'html.parser')
each_person = soup.find_all('tr')
next = 0

for idx, person in enumerate(each_person):
    if idx <= 2:
        continue
    if person.a.contents[0][0:5] == 'http:':
        url = 'https://ideone.com/plain' + person.a.contents[0][17:]
    else:
        url = 'https://ideone.com/plain' + person.a.contents[0][18:]
    td = person.find_all('td')
    #for t in td:
    #    print(t)
    name = td[1].contents
    id = td[2].contents
    comment = td[5].contents
    print('\n\n==========')
    print(idx-1)
    print(name)
    print(id)
    print(comment)
    #print(url)
    print()

    if next > 0:
        next -= 1
        continue
    else:
        x = input("Waiting for press Enter to start... \n or input number n to skip next n \n")
        if len(x) != 0:
            next = int(x)
            continue
    code = requests.get(url).text
    #print(code)
    try:
        exec(code)
        #time.sleep(2)
        gui.hotkey('alt', 'F')
        time.sleep(0.2)
        gui.press('X')
        time.sleep(0.2)
        gui.press('n')
    except:
        print('===== Bad Code =====')
        print(code)
        continue
