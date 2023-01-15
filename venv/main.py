import pyautogui
import pyperclip
import time

#  pyautogui.click
#  pyautogui.write
#  pyautogui.press
#  pyautogui.hotkey

pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://vonkoln.github.io/alea')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
# pyautogui.PAUSE = 5
time.sleep(2)
pyautogui.click(x=697, y=437)


time.sleep(8) 
pyautogui.click(x=636, y=633) 

# nums = []

# while len(nums) < 4:
#     print(i)
#     i += 1



# print(pyautogui.position())







# pyautogui.press('win')
# pyautogui.write('google')
# pyautogui.press('enter')
# time.sleep(5)
# pyautogui.write('google planilha')
# pyautogui.press('enter')
