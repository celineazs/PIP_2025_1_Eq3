#Inchlude <Servo.h>

Servo serv;
int pot=A0;

void setup() {
  // put your setup code here, to run once:
  Serv.attach(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  int v= analogRead(pot); //0-255
  v=map(v,0,1023,0,180);
  Serv.write(v);
  delay(30);
    }
}


