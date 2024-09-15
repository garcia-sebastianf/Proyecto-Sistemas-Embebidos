#!/usr/bin/env python3

import serial
import time
import board
import threading
import queue
import busio
import adafruit_adxl34x
import math
import requests

def Promedio(ColaDatos,ColaVentana,ColaPromedio,ser,conexion_serial):
    N_str = "9"
    print("ValorInicialVentana:",N_str)
    try:

        while True:
            # print("EsperandoLlegadaCaracter")
            #RecibeDatoEnviadoPorUsuario

            #if conexion_serial.in_waiting > 0:
            #    N_str = conexion_serial.read().decode('utf-8')

            if N_str.isdigit() and 1 <= int(N_str) <= 9:
                # Si es un dígito y está en el rango del 1 al 9, convierte a entero
                N_entero = int(N_str)
                print("ValorVentana:",N_entero)
                Promedio = 0
                for i in range(1, N_entero+1):
                    ValorAceleracion = ColaDatos.get() #Espera hasta que llegue el dato de la aceleración
                    Promedio = Promedio + ValorAceleracion/N_entero
                CadenaPromedio = str(Promedio)
                #Envia dato valor del promedio por puerto serial
                ser.write(CadenaPromedio.encode('utf-8'))
                print("Promedio:",Promedio)

                #Enviar a Thinkspeak
                enviar = requests.get("https://api.thingspeak.com/update?api_key=06V20NJIU6CMDLF7&field1="+str(Promedio))
                ColaPromedio.put(Promedio)
                ColaVentana.put(N_entero)

    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para cerrar la conexión serial
        conexion_serial.close()
        print("Conexión serial cerrada.")


def LecturaDatos(ColaDatos):
    # Configura la interfaz I2C
    i2c = busio.I2C(board.SCL, board.SDA)

    # Inicializa el sensor ADXL345
    accelerometer = adafruit_adxl34x.ADXL345(i2c)

    # Bucle principal
    while True:
        # Lee los datos del sensor
        x, y, z = accelerometer.acceleration
        MagAcceleration = math.sqrt(x**2 + y**2 + z**2)

        ColaDatos.put(MagAcceleration)
        # Muestra los datos
        print(f"Aceleración - Value: {MagAcceleration:.2f}")

        #Espera 1 segundo
        time.sleep(0.1)

def CreacionTrama(ColaVentana,ColaPromedio):
    while True:
        Ventana = ColaVentana.get()  #int
        Promedio = ColaPromedio.get() #float
        Trama = f"##PROMEDIO-{str(Ventana) * 3}-{Promedio:.2f}-##\n"
        # Imprimir la cadena
        print(Trama)

print("Aqui defino mis variable")
puerto_serial = '/dev/ttyS0'
tasa_transmision = 115200

# Configuracion del puerto serie lectura (Dato valor promedio)
conexion_serial = serial.Serial(puerto_serial, tasa_transmision)
# Configuración del puerto serie escritura (Dato ventana promedio)
ser = serial.Serial('/dev/ttyS0', tasa_transmision)

ColaDatos      = queue.Queue()
ColaVentana    = queue.Queue()
ColaPromedio   = queue.Queue()

#Creamos los hilos productor y consumidor
hilo_LecturaDatos  = threading.Thread(target=LecturaDatos  ,args=(ColaDatos,))
hilo_Promedio      = threading.Thread(target=Promedio      ,args=(ColaDatos,ColaVentana,ColaPromedio,ser,conexion_serial))
hilo_CreacionTrama = threading.Thread(target=CreacionTrama ,args=(ColaVentana,ColaPromedio))

#Iniciamos los hilos
hilo_LecturaDatos.start()
hilo_Promedio.start()
hilo_CreacionTrama.start()



