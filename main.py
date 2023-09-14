#código para capturar imagem de um celular caso for detectado e salvar nos arquivos e enviar para whatApp do contato selecionado

#bibliotecas utilizadas
import cv2  
import time
import pyautogui
from modulos.abrirPaginaNotebook import abrirPaginaNotebook
from modulos.anexarArquivoNotebook import anexarArquivoNotebook
from modulos.fecharWebCam import fecharWebCam

def salvarFoto():
     cv2.imwrite("aaa_imagem.jpg", frame)

def abrirWebCam():  
     global cap, winName
     #cria uma janela para abrir a webCam
     winName = 'Janela WebCam'
     cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
     cv2.setWindowProperty(winName, cv2.WND_PROP_VISIBLE, cv2.WINDOW_FULLSCREEN)
     #acessa a câmera nesse endereço de ip
     cap = cv2.VideoCapture(0)

def teste():
      time.sleep(5)
      currenrMouseX, currentMouseY = pyautogui.position()
      print(currenrMouseX, currentMouseY)
      time.sleep(20)
#teste()

#chamada a função para abrir página
abrirPaginaNotebook()

#cores nos retangulos
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

#carrega as classes
class_names = []
with open("arquivos\coco.names", "r")as f:
    class_names = [cname.strip() for cname in f.readlines()]

net = cv2.dnn.readNet('arquivos\yolov4-tiny.weights', 'arquivos\yolov4-tiny.cfg')

print("abrindo web cam")

#__________________________________________________________
#opções de carregar video ou webCam
#cap = cv2.VideoCapture("IdentificadorObjetos/futebol.mp4")
#video = cv2.VideoCapture(0)
#__________________________________________________________


#chama função para abrir webCam
abrirWebCam()

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

print("web cam aberta") 


#lendo os frames
while True:
     #capturando frame     
     _, frame = cap.read()
     
     #começo da contagem dos ms
     start = time.time()

     #detecção 
     classes, scores, boxes = model.detect(frame, 0.1, 0.2)

     #fim da contagem dos ms
     end = time.time()

     #percorrer toda detecção
     for (classid, score, box) in zip(classes, scores, boxes):

                    #gerando a color na classe
                    color = COLORS[int(classid) % len (COLORS)]

                    #pegando o nome da classe e aemazena na variável
                    label = f"{class_names[classid]} : {score}" 
                    verificacao = class_names[classid]  
                    tudoOk= ""

                    #desenhando um box na detecção
                    cv2.rectangle(frame, box, color, 2)

                    #escreve o nome da classe em cima do objeto
                    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                    #caso for detectado um celular inicia o processo de captura e envio para whatAppWeb
                    if verificacao == "cell phone":
                        fecharWebCam()  
                        print("Objeto detectado, câmera fechada, iniciando processo...")
                        time.sleep(2)
                        salvarFoto()
                        print("Foto salva OK")
                        print("Anexando foto no contato...")
                        anexarArquivoNotebook()
                        print("Foto enviada OK") 
                        time.sleep(3)
                        print("Abrindo webcam...") 
                        abrirWebCam()    
                        print("Webcam aberta OK")                  
                    else:
                        cv2.putText(frame, tudoOk, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (34, 139, 34), 3)                                     
    
     #mostra vídeo
     cv2.imshow(winName, frame)
 
     #espera da resposta
     if cv2.waitKey(1) == 27:
           break 
 
 #fecha todas as janelas
cap.release()
cv2.destroyAllWindows()




