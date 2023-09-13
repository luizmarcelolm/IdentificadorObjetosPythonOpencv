
import pyautogui
import time


def abrirPaginaNotebook():
     print("abrindo pagina")
     time.sleep(5)
     currenrMouseX, currentMouseY = pyautogui.position()
     pyautogui.doubleClick(49, 38)
     time.sleep(12)
     print("selecionando contato")
     pyautogui.click(293, 263);pyautogui.typewrite("Marcelo Notifica", interval=0.5)  
     print("contato selecionado")
     pyautogui.click(263, 434)
     time.sleep(2)
     print("whatappWeb aberto com contato selecionado")  