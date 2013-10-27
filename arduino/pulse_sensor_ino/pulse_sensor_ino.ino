
int IRled = 13;


void setup() {
  Serial.begin(9600);
  pinMode(IRled, OUTPUT);
}


void loop() {
  
  digitalWrite(IRled, HIGH);
  while(true) {
    if(analogRead(A0)) {
      Serial.println(analogRead(A0));
    } else {
      Serial.println("0");
    }
    delay(2); 
  }


}
