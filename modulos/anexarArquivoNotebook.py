import pyautogui
import time

def anexarArquivoNotebook():
      currenrMouseX, currentMouseY = pyautogui.position()
      pyautogui.click(682, 959)
      time.sleep(2)
      pyautogui.click(773, 685)
      time.sleep(2)
      pyautogui.doubleClick(323, 204)
      time.sleep(2)
      pyautogui.click(1842, 930)
      