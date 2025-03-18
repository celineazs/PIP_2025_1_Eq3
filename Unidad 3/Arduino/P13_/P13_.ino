int pot = A0;
int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
  pinMode(led1, OUTPUT)
  pinMode(led2, OUTPUT)
  pinMode(led3, OUTPUT)
  pinMode(led4, OUTPUT)

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    int v1 = analogRead(pot);
    v1 = map(v,0,1023,0,255);
    switch(v){
      case v1:
        digitalWrite(led1, 1);
        break;
      case :
        digitalWrite(led1, 1);
        break;
      case :
        digitalWrite(led1, 1);
        break;
      case :
        digitalWrite(led1, 1);
        break;
    }
    //Serial.println(v);
    //delay(100);
  }

}
