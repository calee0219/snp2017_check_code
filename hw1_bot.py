import requests
from bs4 import BeautifulSoup as bs
import pyautogui as gui
import time

list_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRuYE3O_dwNvJHKXJAU-iH7p1qoV5xM0uMXq6lAog7dfYy2aDv1xOacRREcCwePoGaUcVe5bHGlBLQL/pubhtml'

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
    #print(td)
    name = td[2].contents
    id = td[3].contents
    comment = td[6].contents
    task = td[7].contents
    print('\n\n==========')
    print(idx-1)
    print(name)
    print(id)
    print(task)
    print(comment)
    #print(url)
    print()
	
    if next > 0:
        next -= 1	
        continue
    else:
        x = input("Waiting for press Enter to start...")
        if len(x) != 0:
            next = int(x)	
            continue		
    code = requests.get(url).text
    #print(code)
    exec(code)
    #time.sleep(2)
    gui.hotkey('alt', 'F')
    time.sleep(0.2)
    gui.press('X')
    time.sleep(0.2)
    gui.press('n')
