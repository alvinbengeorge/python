import pyautogui
import time
import cv2
from pynput.keyboard import Key,Controller
import datetime
start=time.time()
pyautogui.pause=0
keyboard=Controller()
def condition():
    if pyautogui.locateOnScreen("entrar home.png",confidence=0.4)==None:
        d=pyautogui.locateCenterOnScreen("Login1.png",confidence=0.6)
        pyautogui.click(d)
        d=pyautogui.locateCenterOnScreen("Login1.png",confidence=0.6)
        pyautogui.click(d)
def refresh():
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release(Key.ctrl)
    keyboard.release('r')
keyboard.press(Key.cmd)
keyboard.press('1')
keyboard.release(Key.cmd)
keyboard.release('1')
time.sleep(1.5)
s=pyautogui.locateCenterOnScreen("entrar tab.png",confidence=0.7)
pyautogui.click(s)
if pyautogui.locateOnScreen("entrar section.png",confidence=0.5)==None and pyautogui.locateCenterOnScreen("entrar tab.png",confidence=0.7)==None:
    x=0
    while pyautogui.locateOnScreen("Google home page.png",confidence=0.7)==None and x<6:
        time.sleep(1)
        x+=1
    if pyautogui.locateOnScreen("Google home page.png",confidence=0.7)==None:        
        keyboard.press(Key.ctrl)
        keyboard.press('t')
        keyboard.release(Key.ctrl)
        keyboard.release('t')
        if pyautogui.locateOnScreen("Google home page.png",confidence=0.7)==None:
            keyboard.press(Key.cmd)
            keyboard.press('1')
            keyboard.release(Key.cmd)
            keyboard.release('1')
            if pyautogui.locateOnScreen("Google home page.png",confidence=0.7)==None:
                keyboard.press(Key.ctrl)
                keyboard.press('t')
                keyboard.release(Key.ctrl)
                keyboard.release('t')                
    time.sleep(2)
    c=pyautogui.locateCenterOnScreen("searchbar.png", confidence=0.2)
    pyautogui.click(c)
    web="entrar.in/login/login"
    time.sleep(0.3)
    for i in web:
        keyboard.press(i)
        keyboard.release(i)
    keyboard.press(Key.enter)
    x=0
    while pyautogui.locateOnScreen("Login.png",confidence=0.7)==None and x<10:
        time.sleep(1)        
        x+=1
    condition()
    while pyautogui.locateOnScreen("entrar home.png",confidence=0.4)==None:
        time.sleep(1)
        if pyautogui.locateOnScreen("internet error.png",confidence=0.6)!=None:
            refresh()
            condition()
e=pyautogui.locateCenterOnScreen("online classroom.png",confidence=0.6)
pyautogui.click(e)
y=0
while True:
    time.sleep(1)
    y+=1
    if y%20==0:
        refresh()
    e=pyautogui.locateCenterOnScreen("Join button.png",confidence=0.9)
    time.sleep(2)
    if e!=None:
        pyautogui.click(e)
        pyautogui.click(e)
        break
x=0
while pyautogui.locateOnScreen("listen only.png",confidence=0.9)==None and x<10:
        time.sleep(1)
e=pyautogui.locateCenterOnScreen("listen only.png",confidence=0.9)
pyautogui.click(e)
end=time.time()

    

