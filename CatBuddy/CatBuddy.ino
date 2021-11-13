#include <Servo.h>

#define CAMERA_ELEVATION 550             //height of camera relative to ground, dm
#define CAMERA_ZONE_DISTANCE 75          //distance from the active zone to the camera on the y axis, dm
#define ZONE_WIDTH 2                     //width of active zone, m
#define ZONE_HEIGHT 7                    //height of active zone, m
#define SERVO_DELAY 20                   //delay between signals to motor, ms
#define TERMINATOR_CHAR '|'              //terminator for serial inputs, char
#define BAUD 9600

Servo servoHorizontal;
Servo servoVertical;

int angleHorizontal, angleVertical;
int shPin = 5, svPin=4;

void setup()
{
  // init servo motors
  //  angleHorizontal = 0;
  //  servoHorizontal.attach(shPin); // pwm pin 5
  //  servoHorizontal.write(angleHorizontal);
  //
  //  angleVertical = 0;
  //  servoVertical.attach(svPin); // pwm pin 4
  //  servoVertical.write(angleVertical);

  //start up nvidia apu
  Serial.begin(BAUD);

  while (!Serial) {} // wait for serial port to connect.
}

void loop()
{
  if(Serial.available() > 0)
  {
    String serialInput = Serial.readStringUntil(TERMINATOR_CHAR);
    Serial.print("Reciev   ed: " + serialInput + "\n");
    Serial.flush();
    // parse string to set horizontal and vertical angle 
  }
   //moveToHorizontal(angleHorizontal);
   // moveToVertical(angleVertical);
  
    //  angleHorizontal += 5;
    //  angleVertical +=5;
    //
    //  if(angleHorizontal == 180) angleHorizontal = 0;
    //
    //  if(angleVertical == 180) angleVertical = 0;


  //get all object detections, previously filtered out to only cats
  //from data, get target cat
  //get coordinates on screen of target cat's centeraw
  //get location of laser on screen
  //if cat is near location, pick random location
  //calculate angle for new location
  //send function to move to new angle

  delay(SERVO_DELAY); 
}

//-----------------------------------------------------------------------probably should put these somewhere else
void moveToHorizontal(int angle)
{
  servoHorizontal.write(angle);
  angleHorizontal = angle;
}

void moveToVertical(int angle)
{
  servoVertical.write(angle);
  angleVertical = angle;
}
