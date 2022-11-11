int i =10;
void setup() {
Serial.begin(9600);
}

void loop() {
  if (i>0){
    Serial.println(i);
    i=i-1;
    }
   else{
    i=10;
    }
   delay(1000); // waits for a second

}
