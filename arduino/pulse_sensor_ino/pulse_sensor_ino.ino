
int IRled = 13;
int ret = 0;
String buff = "";
int c = 0;

void setup() {
  Serial.begin(115200);
  pinMode(IRled, OUTPUT);
}


void loop() {
  digitalWrite(IRled, HIGH);
  while(true) {
    if(analogRead(A0)) {
      ret = (int) analogRead(A0);
      //Serial.println(ret);                  
      buff.concat(ret);
      buff.concat(",");
      //Serial.println(c);
      if(c == 25) {
        c = 0;
        Serial.println(buff);
        ret = 0;
        //Serial.println(c);
      } else {
        c++;
      }      
    } else {
      Serial.println("0");
    }
    delay(250);
  }
}

