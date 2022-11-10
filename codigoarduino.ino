#include <SoftwareSerial.h>
SoftwareSerial mySerial(2,3); 
int sinalSensor = 0;
int sensor = A0;
void setup()
{
    pinMode(sensor,INPUT);  
    Serial.begin(9600);
    mySerial.begin(9600);
}
void loop()
{
  sinalSensor = analogRead(sensor); 
  Serial.println(sinalSensor);
  delay(200);
  mySerial.println(sinalSensor);
}
