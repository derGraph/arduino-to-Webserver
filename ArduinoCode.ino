void setup() {
Serial.begin(9600);
while(!Serial){}
}
int i=0;
void loop() {
i++;
Serial.print(i);
Serial.print(",");
Serial.println(i/2);
delay(2000);
}
