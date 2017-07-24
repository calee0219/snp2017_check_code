#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pyautogui
import time

pyautogui.FAILSAFE = True

# open url
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
time.sleep(0.2)
pyautogui.typewrite('https://goo.gl/forms/qctR7aDpw6C5pi492')
pyautogui.press('enter')
time.sleep(1)

name_loc = pyautogui.locateOnScreen('name.png')
pyautogui.click(name_loc[0]+20, name_loc[1]+20)
# pyautogui.typewrite('李家安')
pyautogui.typewrite('Gavin Lee')
