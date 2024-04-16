#!/usr/bin/env python3

import serial
import time

# Configuración del puerto serie
ser = serial.Serial('/dev/ttyS0', 115200)

try:
    while True:
        #Envío del caracter 'a'
        #ser.write(b'Hola')
        ser.write("Hola".encode('Ascii'))
        # time.sleep(0.1)
        #Espera bree (ajusta según sea necesario)

finally:
    #Este bloque se ejecutará solo si hay alguna excepción
    #Cierra el puerto serie antes de salir.
    ser.close()


