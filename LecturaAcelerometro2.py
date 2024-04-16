#!/usr/bin/env python3

import time
import board
import busio
import adafruit_adxl34x
import math

# Configura la interfaz I2C

i2c = busio.I2C(board.SCL, board.SDA)

# Inicializa el sensor ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# Bucle principal
while True:
    # Lee los datos del sensor
    x, y, z = accelerometer.acceleration
    MagAcceleration = math.sqrt(x**2 + y**2 + z**2)
    # Muestra los datos
    print(f"Aceleración - Value: {MagAcceleration:.2f}")

    # Espera 1 segundo
    #time.sleep(1)

