#include <LiquidCrystal_I2C.h>
#include <Wire.h>

// pantalla LCD I2C, puede que sea 0x27 o 0x3F
LiquidCrystal_I2C lcd(0x27, 16, 2);

// sensores y actuadores
int sensorPIR = 2;
int sensorMag = 3;
int sensorLuz = A0;
int buzzer = 8;

// leds
int led1 = 6;
int led2 = 7;
int led3 = 9;
int led4 = 10;

int limiteLuz = 300;

// alarmas
bool hayMovimiento = false;
bool puertaAbierta = false;
bool sonidoActivo = false;
bool haciendoBeep = false;
int tipoAlarma = 0;
int beeps = 0;
unsigned long ultimoBeep = 0;

void setup() {
  pinMode(sensorPIR, INPUT);
  pinMode(sensorMag, INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Cargando...");
  delay(1000);
  lcd.clear();

  Serial.begin(9600);
  Serial.println("Sistema iniciado");
}

void loop() {
  int mov = digitalRead(sensorPIR);
  int puerta = digitalRead(sensorMag);
  int luz = analogRead(sensorLuz);

  Serial.print("Movimiento: ");
  Serial.println(mov);
  Serial.print("Luz: ");
  Serial.println(luz);

  // luces automáticas
  if (luz < limiteLuz) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    digitalWrite(led4, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("Noche: Luces ON ");
  } else {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led4, LOW);
    lcd.setCursor(0, 1);
    lcd.print("Dia: Luces OFF  ");
  }

  // si detecta movimiento y no está sonando ya
  if (mov == HIGH && !sonidoActivo) {
    lcd.setCursor(0, 0);
    lcd.print("Hay moviviento afuera!!    ");
    Serial.println("Movimiento!!");
    hayMovimiento = true;
    tipoAlarma = 1;
    sonidoActivo = true;
    beeps = 0;
    ultimoBeep = millis();
  }

  // si se abre la puerta
  if (puerta == HIGH && !sonidoActivo) {
    lcd.setCursor(0, 0);
    lcd.print("Puerta abierta!");
    Serial.println("Alerta: puerta abierta");
    puertaAbierta = true;
    tipoAlarma = 2;
    sonidoActivo = true;
    beeps = 0;
    ultimoBeep = millis();
  }

  // control del buzzer
  if (sonidoActivo) {
    unsigned long actual = millis();

    if (tipoAlarma == 1) {
      if (actual - ultimoBeep >= 200) {
        if (haciendoBeep) {
          noTone(buzzer);
          haciendoBeep = false;
          beeps++;
        } else {
          tone(buzzer, 1000);
          haciendoBeep = true;
        }
        ultimoBeep = actual;
      }
      if (beeps >= 3) {
        noTone(buzzer);
        sonidoActivo = false;
        lcd.setCursor(0, 0);
        lcd.print("                ");
      }
    }

    if (tipoAlarma == 2) {
      if (actual - ultimoBeep < 1000) {
        tone(buzzer, 500);
      } else {
        noTone(buzzer);
        sonidoActivo = false;
        lcd.setCursor(0, 0);
        lcd.print("                ");
      }
    }
  }

  // mensaje de bienvenida si todo está tranquilo
  if (!sonidoActivo && !hayMovimiento && !puertaAbierta) {
    lcd.setCursor(0, 0);
    lcd.print("Todo OK :)      ");
  }

  delay(50);
}
