int pot = A0;
int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    int v1 = analogRead(pot);
    v1 = map(v1, 0, 1023, 0, 4);
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);

    switch(v1){
      case 0 :
        digitalWrite(led1, 1);
        break;
      case 1 :
        digitalWrite(led2, 1);
        break;
      case 2 :
        digitalWrite(led3, 1);
        break;
      case 3 :
        digitalWrite(led4, 1);
        break;
    }
    Serial.println(v1);
    delay(100);
  }

}
