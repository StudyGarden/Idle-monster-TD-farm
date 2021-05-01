from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    #mapa1

##    if pyautogui.locateOnScreen('map1.png', confidence=0.99) !=None:
##        pyautogui.click('load.png')
##        time.sleep(1)
##        pyautogui.click('load2.png')        
##        print('Campeões adicionados ao map1!')
##
##        #mapa2
##
##    elif pyautogui.locateOnScreen('map2.png', confidence=0.99) !=None:
##        pyautogui.click('load.png')
##        time.sleep(1)
##        pyautogui.click('load2.png')        
##        print('Campeões adicionados ao map2!')
##
##        #map3
##        
##    elif pyautogui.locateOnScreen('map3.png', confidence=0.99) !=None:
##        pyautogui.click('load.png')
##        time.sleep(1)
##        pyautogui.click('load2.png')        
##        print('Campeões adicionados ao map3!')
##
##        #mapa4
##
##    elif pyautogui.locateOnScreen('map4.png', confidence=0.99) !=None:
##        pyautogui.click('load.png')
##        time.sleep(1)
##        pyautogui.click('load2.png')        
##        print('Campeões adicionados ao map4!')

        
    if pyautogui.locateOnScreen('h1.png', confidence=0.80) !=None:
        click(541, 658)
        time.sleep(1)
        print('habilidade 1 pressionada')
    elif pyautogui.locateOnScreen('h2.png', confidence=0.80) !=None:
        click(609, 658)
        time.sleep(1)
        print('habilidade 2 pressionada')       
    elif pyautogui.locateOnScreen('h3.png', confidence=0.80) !=None:
        click(667, 658)
        time.sleep(1)
        print('habilidade 3 pressionada')
    elif pyautogui.locateOnScreen('h4.png', confidence=0.80) !=None:
        click(726, 658)
        time.sleep(1)
        print('habilidade 4 pressionada')
        #wave prestige
    elif pyautogui.locateOnScreen('wave1335.png', confidence=0.99) !=None:
        pyautogui.click('pronp.png')
        pyautogui.click('prestige.png')
        time.sleep(1)
        pyautogui.click('lets.png')        
        print('Prestige start wave 1335')
        time.sleep(10)
    elif pyautogui.locateOnScreen('wave1347.png', confidence=0.99) !=None:
        pyautogui.click('pronp.png')
        pyautogui.click('prestige.png')
        time.sleep(1)
        pyautogui.click('lets.png')        
        print('Prestige start wave 1347')

    elif pyautogui.locateOnScreen('box.png', confidence=0.80) !=None:
        click(562, 73)
        time.sleep(1)
        click(807, 132)
        time.sleep(1)
        click(753, 328)
        
        

        
