int potenciometro = A0;
int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valor = analogRead(potenciometro);
  Serial.print(valor);
  delay(100)

  // E2 IZQ - DER -- punto medio -- DER-IZQ
  

}
