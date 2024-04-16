#!/usr/bin/env python3
import serial
import time

puerto_serial ="/dev/ttyS0"  # Ajusta el nombre del puerto según sea necesario
tasa_transmision = 115200

conexion_serial = serial.Serial(puerto_serial, tasa_transmision)

try:
    while True:
        # print("EsperandoLlegadaCaracter")
        N = conexion_serial.read().decode('utf-8')
        print("Línea recibida:",N)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C) para cerrar la conexión serial
    conexion_serial.close()
    print("Conexión serial cerrada.")

