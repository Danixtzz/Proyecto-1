from machine import Pin, I2C
import time
import bme280_float

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
sensor = bme280_float.BME280(i2c=i2c, address=0x76)

print("Sensor activo. STOP para terminar.")
try:
    n = 1
    while True:
        t, p, h = sensor.values
        print(f"{n:3d}: {t:8s} {p:10s} {h:7s}")
        n += 1
        time.sleep(1)
except:
    print(f"Fin. Lecturas: {n-1}")     