#função que abre página whatapp web e faz pesquisa do contato

import pyautogui
import time


def abrirPaginaMonitor():
     print("abrindo pagina")
     time.sleep(10)
     currenrMouseX, currentMouseY = pyautogui.position()
     pyautogui.doubleClick(48, 42)
     time.sleep(20)
     print("selecionando contato")
     pyautogui.click(608,-662);pyautogui.typewrite("Marcelo Notifica", interval=0.6)
     time.sleep(6)  
     print("contato selecionado")
     pyautogui.doubleClick(635, -507)
     time.sleep(2)
     print("whatappWeb aberto com contato selecionado")  