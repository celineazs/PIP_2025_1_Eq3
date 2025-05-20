rconst int leds[] = {9, 8, 7, 6, 5, 4, 3, 2}; 
int numero; 

void setup() {
    Serial.begin(9600);  
    Serial.println("Ingresa un numero entre 0 y 255:");

    for (int i = 0; i < 8; i++) {
        pinMode(leds[i], OUTPUT); 
    }
}

void loop() {
    if (Serial.available() > 0) {  
        numero = Serial.parseInt();  
        if (numero > 0 && numero <= 255) {  
            Serial.print("Numero ingresado: ");
            Serial.println(numero);

            for (int i = 0; i < 8; i++) {
                int bit = numero % 2;
                digitalWrite(leds[i], bit);  
                numero = numero / 2;  
            }
          delay(5000);
          for (int i = 0; i < 8; i++) {
            digitalWrite(leds[i], 0);
          }
        } else {
            Serial.println("Error: Ingresa un numero entre 0 y 255.");
        }
    }
}