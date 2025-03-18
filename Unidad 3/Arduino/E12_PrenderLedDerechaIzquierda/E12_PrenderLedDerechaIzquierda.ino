int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  // Encender de izquierda a derecha
  digitalWrite(led1, 1);
  delay(200);
  digitalWrite(led2, 1);
  delay(200);
  digitalWrite(led3, 1);
  delay(200);
  digitalWrite(led4, 1);
  delay(200);
  digitalWrite(led5, 1);
  delay(200);

  // Apagar de izquierda a derecha
  digitalWrite(led1, 0);
  delay(200);
  digitalWrite(led2, 0);
  delay(200);
  digitalWrite(led3, 0);
  delay(200);
  digitalWrite(led4, 0);
  delay(200);
  digitalWrite(led5, 0);
  delay(200);

  // Encender de derecha a izquierda
  digitalWrite(led5, 1);
  delay(200);
  digitalWrite(led4, 1);
  delay(200);
  digitalWrite(led3, 1);
  delay(200);
  digitalWrite(led2, 1);
  delay(200);
  digitalWrite(led1, 1);
  delay(200);

  // Apagar de derecha a izquierda
  digitalWrite(led5, 0);
  delay(200);
  digitalWrite(led4, 0);
  delay(200);
  digitalWrite(led3, 0);
  delay(200);
  digitalWrite(led2, 0);
  delay(200);
  digitalWrite(led1, 0);
  delay(200);
}
