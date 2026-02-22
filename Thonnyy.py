from machine import Pin, I2C      # Importa clases para manejar pines GPIO y comunicación I2C (en MicroPython)
import time                       # Importa funciones de tiempo (por ejemplo, sleep)
import bme280_float               # Importa la librería del sensor BME280 (versión que da valores en float/formato legible)

# Crea el bus I2C en el canal 0
# scl=Pin(22) -> pin para la línea de reloj (SCL)
# sda=Pin(21) -> pin para la línea de datos (SDA)
# freq=100000 -> frecuencia del bus I2C (100 kHz, valor común/seguro)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

# Inicializa el sensor BME280 usando el bus I2C creado
# address=0x76 -> dirección I2C del sensor (algunos módulos usan 0x77)
sensor = bme280_float.BME280(i2c=i2c, address=0x76)

print("Sensor activo. STOP para terminar.")   # Mensaje inicial para indicar que el programa está corriendo

try:
    n = 1                                      # Contador de lecturas (empieza en 1)

    while True:                                # Bucle infinito: seguirá leyendo hasta que se detenga manualmente
        t, p, h = sensor.values                # Lee valores del sensor: temperatura (t), presión (p), humedad (h)
                                               # sensor.values normalmente devuelve strings con unidades (ej. "24.5C")

        print(f"{n:3d}: {t:8s} {p:10s} {h:7s}")
        
        

        n += 1                                 # Incrementa el contador para la siguiente lectura

        time.sleep(1)                          # Espera 1 segundo antes de volver a leer (1 Hz)

except:
    # Si ocurre un error o se detiene manualmente (por ejemplo Ctrl+C / STOP en Thonny),
    # muestra cuántas lecturas se alcanzaron a hacer
    print(f"Fin. Lecturas: {n-1}")