const int leds[] = {9, 8, 7, 6, 5, 4, 3, 2}; 
char letra;
int numero;

void setup() {
    Serial.begin(9600);  
    Serial.println("Ingresa una palabra (solo letras mayúsculas A-Z):");

    for (int i = 0; i < 8; i++) {
        pinMode(leds[i], OUTPUT); 
    }
}

void loop() {
    if (Serial.available() > 0) {  
        letra = Serial.read();  
        if (letra >= 'A' && letra <= 'Z') {  
            numero = (int)letra;  
            Serial.print("Letra ingresada: ");
            Serial.println(letra);
            Serial.print("Código ASCII: ");
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
            Serial.println("Error: Ingresa solo letras mayúsculas (A-Z).");
        }
    }
}

