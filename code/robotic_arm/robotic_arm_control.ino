#include <Servo.h>

Servo servothumb;          // Define thumb servo
Servo servoindex;          // Define index servo
Servo servomajeure;
Servo servoringfinger;
Servo servopinky;
Servo servowrist;


void setup() {
  servothumb.attach(5);  // Set thumb servo to digital pin 2
  servoindex.attach(9);  // Set index servo to digital pin 3
  servomajeure.attach(10);
  servoringfinger.attach(3);
  servopinky.attach(6);
  servowrist.attach(11);
}


void loop() {            // Loop through motion tests
//  servomajeure.write(0);
  alltovirtual();        // Example: alltovirtual
  delay(2000);           // Wait 4000 milliseconds (4 seconds)
  alltorest();           // Uncomment to use this
  delay(2000);           // Uncomment to use this
  alltomax();            // Uncomment to use this
  delay(2000);           // Uncomment to use this
}


// Motion to set the servo into "virtual" 0 position: alltovirtual
void alltovirtual() {        
  servothumb.write(0);
  servoindex.write(0);
  servomajeure.write(0);
  servoringfinger.write(0);
  servopinky.write(0);
//  servowrist.write(0);
}


// Motion to set the servo into "rest" position: alltorest
void alltorest() {        
  servothumb.write(0);
  servoindex.write(0);
  servomajeure.write(0);
  servoringfinger.write(0);
  servopinky.write(0);
//  servowrist.write(0);
}


// Motion to set the servo into "max" position: alltomax
void alltomax() {
  servothumb.write(180);
  servoindex.write(180);
  servomajeure.write(180);
  servoringfinger.write(180);
  servopinky.write(180);
//  servowrist.write(180);
}
