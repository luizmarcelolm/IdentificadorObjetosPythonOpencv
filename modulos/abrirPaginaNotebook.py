
import pyautogui
import time


def abrirPaginaNotebook():
     print("Abrindo página...")
     time.sleep(5)
     currenrMouseX, currentMouseY = pyautogui.position()
     pyautogui.doubleClick(49, 38)
     time.sleep(12)
     print("Página aberta OK")
     print("Selecionando contato...")
     pyautogui.click(293, 263);pyautogui.typewrite("Marcelo Notifica", interval=0.5)   
     pyautogui.click(263, 434)
     time.sleep(2)
     print("Contato selecionado OK")  