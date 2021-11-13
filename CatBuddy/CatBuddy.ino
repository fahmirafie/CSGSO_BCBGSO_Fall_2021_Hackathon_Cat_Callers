#define CAMERA_ELEVATION 550             //height of camera relative to ground, dm
#define CAMERA_ZONE_DISTANCE 75          //distance from the active zone to the camera on the y axis, dm
#define ZONE_WIDTH 2                     //width of active zone, m
#define ZONE_HEIGHT 7                    //height of active zone, m

void setup()
{
  Serial.begin(9600);
  //start up nvidia apu
  Serial.println("setup phase");
}

void loop()
{
  // put your main code here, to run repeatedly:
  Serial.println("loop phase");
  delay(100); 

  // real code starts here
  //get all object detections, previously filtered out to only cats
  //from data, get target cat
  //get coordinates on screen of target cat's center
  //get location of laser on screen
  
}
