
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
      Serial.println(ret);
     //buff.concat(ret);
      //buff.concat(",");
      //Serial.println(c);
      /*if(c == 250) {
        c = 0;
        Serial.println(buff);
        //Serial.println(c);
      } else {
        c++;
      }
      */
      //if(ret < 1023) {
        //ret = ret * 10;        
        //Serial.println(analogRead(A0));      
        //  Serial.println(ret);
      //}
     // Serial.println(ret);
       //Serial.println(buff);
    } else {
      Serial.println("0");
    }
    delay(250);
  }
}

/*
void calculate_beat_rate(int rate) {
  int i = 0;
  int buff[200];
  int acc = 0;
  int mem = 0;
  if(rate < 1023) {
    acc += 1;
  } else {
    mem = acc;
    acc = 0;      
  }
}
*/

