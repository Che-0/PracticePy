import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro microfono y devolver el audio en texto 
def transformar_audio():

    # almacenar recognizer en variable
    r = sr.Recognizer()
 
    #configurar micro 
    with sr.Microphone() as origen:

        # tiempo de espera 
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion 
        print("ya puedes empezar a hablar ")

        # guardar lo escuchado
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio,lenguage="es-mx") #español mexico 

            # imprimir lo que se transformo
            print("Dijiste: " + pedido)

            #devolver a pedido
            return pedido

        #error 
        except sr.UnknownValueError:

            #prueba de que no comprendio
            print("no entendi")

            return "sigo esperando"

        #en caso de n resolver el pedido
        except sr.RequestError:
            print("no encontre ni madres")
            return "sigo esperando"

        except:
            print("no se que verga pasó")
            return "sigo esperando"

transformar_audio()