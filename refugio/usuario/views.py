from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import FormularioRegistro,FormularioLogin
from .forms import AxesCaptchaForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from axes.utils import reset_request

import cv2
import os
import imutils
import numpy as np
from axes.backends import AxesBackend


class MyBackend(AxesBackend):
    def authenticate(self, request=None, *args, **kwargs):
        if request:
            return super().authenticate(request, *args, **kwargs)

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def fail(request):
    return render(request, 'usuario/fail.html')

 
def acceder(request):
    if request.method == "POST":
        form = FormularioLogin(request, data=request.POST)
          
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('mascota_listar_imagenes')           
            else:
                messages.error(request, "Los datos son incorrectos aasdfas")
           
        else:
            messages.error(request, "Los datos son incorrectos fdsf")
            

    form = FormularioLogin()
    return render(request, "usuario/acceder.html", {"form": form})

def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("inicio")

class VistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = FormularioRegistro()
        return render(request, 'usuario/registrar.html', {'form': form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form =  FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            #login(request, usuario)
            return redirect("caras")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'usuario/registrar.html', {'form': form})

def ValidarCara(request):
    
    dataPath = '/code/refugio/media/perfil'#Cambia a la ruta donde hayas almacenado Data
    imagePaths = os.listdir(dataPath)
    print('imagePaths =', imagePaths)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    face_recognizer.read('modeloEigenFace.xml')

    
    nombreVentana = "camara"
    cv2.namedWindow(nombreVentana)
    cap = cv2.VideoCapture(0)



    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    while True:
        ret,frame = cap.read()
        if ret == False: 
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        # EigenFaces
            if result[1] < 4500:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                print (imagePaths[result[0]])
                nombre = str(imagePaths[result[0]])
                contexto = {'user': nombre}
                print("rostro detectado exitoso")
                return render(request, 'usuario/rostro_validado.html',contexto)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                nombre = "Desconocido"
                contexto = {'user': nombre}
                return render(request, 'usuario/rostro_invalido.html',contexto) 
        cv2.imshow(nombreVentana,frame)
        k = cv2.waitKey(1)
        if k == 27 or not cv2.getWindowProperty(nombreVentana, cv2.WND_PROP_VISIBLE):
            break

    cap.release()

    cv2.destroyAllWindows(nombreVentana)

   

def RegistroCaras(request):
    #model = User
    nombre = User.objects.all().last()
    contexto = {'user': nombre}
    print("ultimo usuario::  ",nombre)
    
    #contexto = {'mascotas':mascota}
    #aaa = input(" Escriba su nombre de usuario: ")
    personName =  str(nombre)
    
    dataPath = 'code/refugio/media/perfil'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
    
        faces = faceClassif.detectMultiScale(gray,1.3,5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)
    
        k =  cv2.waitKey(1)
        if k == 27 or count >= 50:
            break
    cap.release()
    cv2.destroyAllWindows()

    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')
        for fileName in os.listdir(personPath):
            #print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
            image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
        label = label + 1

    #joseprint('Labels= ',labels)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    face_recognizer.write('modeloEigenFace.xml')
    print("Modelo almacenado...")
    return render(request, 'usuario/caras.html',contexto)

       

    #comparacion(imagen1,imagen2)

    
def locked_out(request):
    if request.method == "POST":
        form = AxesCaptchaForm(request.POST)
        if form.is_valid():
            reset_request(request)
            return HttpResponseRedirect(reverse_lazy('acceder'))
    else:
        form = AxesCaptchaForm()

    return render(request, 'usuario/captcha.html', {'form': form})