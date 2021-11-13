
static const int heartbeat = 13;

void setup()
{
  Serial.begin(9600);
  Serial.println("setup phase");
}

void loop()
{
  // put your main code here, to run repeatedly:
  Serial.println("loop phase");
  delay(100); 
}
