import serial as controlador

# Genera el canal de comunicacion y la inicializa...
arduino = controlador.Serial('COM3', 9600, timeout=1)
while True:
    accion = input("Ingresa el valor de accion para el led")
    arduino.write(accion.encode())




