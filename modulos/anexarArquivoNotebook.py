import pyautogui
import time

def anexarArquivoNotebook():
      currenrMouseX, currentMouseY = pyautogui.position()
      pyautogui.click(682, 959)
      time.sleep(2)
      pyautogui.click(773, 685)
      time.sleep(2)
      pyautogui.doubleClick(127, 160)
      time.sleep(2)
      pyautogui.doubleClick(314, 200)
      time.sleep(2)
      pyautogui.click(1341, 952)
      