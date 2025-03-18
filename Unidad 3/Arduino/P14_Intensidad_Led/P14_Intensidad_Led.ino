int led = 6;
0.
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i<255; i++){
    analogwrite(led, i);// se utiliza siempre que un pin

    delay(0);
    }
  for(int i  =255; i>0; i--){
    analogwrite(led, i);
    delag(10);


    
    }
}


