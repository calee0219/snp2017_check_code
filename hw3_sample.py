import pyautogui
import time

pyautogui.FAILSAFE = True

print('start check')
x, y = pyautogui.size()

# click check box
while True:
    time.sleep(0.2)
    still = False
    for loc in pyautogui.locateAllOnScreen('box.png'):
        still = True
        center = pyautogui.center(loc)
        print(center)
        pyautogui.click(center)
    if still == False:
        break
    print('To Scroll')
    pyautogui.scroll(-1*y//2)

# submit
print('find submit')
loc = pyautogui.locateOnScreen('submit.png')
if loc != None:
    print('find it')
    center = pyautogui.center(loc)
    pyautogui.click(center)
