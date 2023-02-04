import time
import pyautogui
import os
from PIL import ImageGrab
from playsound import playsound
import sys
import dk_wnd_control

os.system("DKNameWall")

code = []
string = 0
filename = sys.argv[1]
file = open(filename, "r")

for line in file:
    code.append(line)
    if 'rightClick' in code[string]:
        pyautogui.rightClick()
    elif 'leftClick' in code[string]:
        pyautogui.leftClick()
    elif 'sleep:' in code[string]:
        time.sleep(float(line[6:]))
    elif 'exit' in code[string]:
        exit()
    elif 'xpose:' in code[string]:
        xpose = float(line[6:])
    elif 'ypose:' in code[string]:
        ypose = float(line[6:])
    elif 'movespeed:' in code[string]:
        speed = float(line[10:])
    elif 'movemouse' in code[string]:
        pyautogui.move(xpose, ypose, speed)
    elif 'writespeed:' in code[string]:
        wrspeed = float(line[11:])
    elif 'write:' in code[string]:
        pyautogui.typewrite(line[6:], wrspeed)
    elif 'open:' in code[string]:
        os.startfile(line[5:])
    elif 'press:' in code[string]:
        pyautogui.press(line[6:])
    elif 'makeScreenshot:' in code[string]:
        pyautogui.screenshot(line[15:])
    elif 'consoleLog:' in code[string]:
        print(line[11:])
    elif 'makeAlert:' in code[string]:
        pyautogui.alert(line[10:])
    elif 'soundPlay:' in code[string]:
        playsound(line[10:])
    elif 'title:' in code[string]:
        dk_wnd_control.WndTitle(line[6:])
    elif 'color:' in code[string]:
        dk_wnd_control.ConsoleColor(line[6:])
    elif 'jmpBegin' in code [string]:
        os.system("dyokey " + filename)
    elif 'jmp:' in code[string]:
        os.system("dyokey " + line[4:])
    elif 'sys:' in code[string]:
        os.system(line[4:])
    string += 1