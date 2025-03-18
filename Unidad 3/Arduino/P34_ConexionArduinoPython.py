import serial as controlador

# Genera el canal de comunicacion y la inicializa...
arduino = controlador.Serial('COM3', 9600, timeout=1)

while True:
    cadena = arduino.readline().decode().strip()
    if cadena != "":
        print(cadena)




