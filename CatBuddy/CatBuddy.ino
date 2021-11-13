#include <Servo.h>
 
#define CAMERA_ELEVATION 550             //height of camera relative to ground, dm
#define CAMERA_ZONE_DISTANCE 75          //distance from the active zone to the camera on the y axis, dm
#define ZONE_WIDTH 2                     //width of active zone, m
#define ZONE_HEIGHT 7                    //height of active zone, m
#define SERVO_DELAY 250                  //delay between signals to motor, ms
#define BAUD 9600 
 
#define H_PIN 12
#define V_PIN 13
int x, y, horizontalAngle, verticalAngle;
Servo horizontalMotor, verticalMotor;
 
/* init motors and serial communication with GPU*/
void setup()
{
    horizontalMotor.attach(H_PIN);
    verticalMotor.attach(V_PIN);
    horizontalMotor.write(0);
    Serial.begin(9600);
    while (! Serial);
}
 
void loop()
{
    /* get alerted of new position */
    if(Serial.available() > 0)
    {
      horizontalAngle += Serial.parseInt();
      verticalAngle  += Serial.parseInt();
    }

    //get cat detection from jetson
    //get coordinates on screen of target cat's center
    //get location of laser on screen
    //if cat is near location, pick random location
    //calculate angle for new location
    //send function to move to new angle
    
    /* update motor angles to get to or stay in desired position */
    horizontalMotor.write(horizontalAngle);
    verticalMotor.write(verticalAngle);
    delay(SERVO_DELAY);
}