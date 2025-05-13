long m;
int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  m = millis();
  int nm = m / 1000;
  Serial.println(String(m) + " " + String(nm));

  if (nm % 2 == 0) {
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }
}
//prender y apagar un led pero sin delay osea con millis

