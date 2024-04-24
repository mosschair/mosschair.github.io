#define LeftMotorSpeedPin 4
#define RightMotorSpeedPin 13

//High is forward
#define LeftMotorDirectionPin 10
#define RightMotorDirectionPin 3


//High is off
#define LeftMotorEnable 11
#define RightMotorEnable 7


double LeftMotorSpeed = 0; //value from -255 <-> +255    with window between -32 <-> +32 all corresponding to 0
double RightMotorSpeed = 0; //value from -255 <-> +255   with window between -32 <-> +32 all corresponding to 0

int MaxSpeed = 255;

int off=0;
double accel=.25;

//RPLidar lidar;

float distance, angle;

  void enable(){
    off = 0;
    analogWrite(LeftMotorEnable,off);
    analogWrite(RightMotorEnable,off);
  }

  void quit()
  {
    off = 255;
    analogWrite(LeftMotorEnable,off);
    analogWrite(RightMotorEnable,off);
  }

  void stop(){
    LeftMotorSpeed = 0;
    RightMotorSpeed = 0;
    if(LeftMotorSpeed < 32 && LeftMotorSpeed >-32){
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, 0);
    }
    else if (LeftMotorSpeed < 0) {
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, -LeftMotorSpeed);
    }
    else {
      analogWrite(LeftMotorDirectionPin, 255);

      analogWrite(LeftMotorSpeedPin, LeftMotorSpeed);

    }
 
    if(RightMotorSpeed < 32&& RightMotorSpeed >32){
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, 0);
    }
    else if (RightMotorSpeed < 0) {
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, -RightMotorSpeed);
    }
    else {
      analogWrite(RightMotorDirectionPin, 255);

      analogWrite(RightMotorSpeedPin, RightMotorSpeed);

    }
  }

  void forward(int speed){
    LeftMotorSpeed = speed;
    RightMotorSpeed = speed;
    if(LeftMotorSpeed < 32 && LeftMotorSpeed >-32){
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, 0);
    }
    else if (LeftMotorSpeed < 0) {
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, -LeftMotorSpeed);
    }
    else {
      analogWrite(LeftMotorDirectionPin, 255);

      analogWrite(LeftMotorSpeedPin, LeftMotorSpeed);

    }
 
    if(RightMotorSpeed < 32&& RightMotorSpeed >32){
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, 0);
    }
    else if (RightMotorSpeed < 0) {
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, -RightMotorSpeed);
    }
    else {
      analogWrite(RightMotorDirectionPin, 255);

      analogWrite(RightMotorSpeedPin, RightMotorSpeed);

    }
  }

  void backward(int speed){
    LeftMotorSpeed = -speed;
    RightMotorSpeed = -speed;
    if(LeftMotorSpeed < 32 && LeftMotorSpeed >-32){
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, 0);
    }
    else if (LeftMotorSpeed < 0) {
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, -LeftMotorSpeed);
    }
    else {
      analogWrite(LeftMotorDirectionPin, 255);

      analogWrite(LeftMotorSpeedPin, LeftMotorSpeed);

    }
 
    if(RightMotorSpeed < 32&& RightMotorSpeed >32){
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, 0);
    }
    else if (RightMotorSpeed < 0) {
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, -RightMotorSpeed);
    }
    else {
      analogWrite(RightMotorDirectionPin, 255);

      analogWrite(RightMotorSpeedPin, RightMotorSpeed);

    }
  }

  void turnRight(int speed){
    LeftMotorSpeed = speed;
    RightMotorSpeed = 0; 
    if(LeftMotorSpeed < 32 && LeftMotorSpeed >-32){
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, 0);
    }
    else if (LeftMotorSpeed < 0) {
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, -LeftMotorSpeed);
    }
    else {
      analogWrite(LeftMotorDirectionPin, 255);

      analogWrite(LeftMotorSpeedPin, LeftMotorSpeed);

    }
 
    if(RightMotorSpeed < 32&& RightMotorSpeed >32){
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, 0);
    }
    else if (RightMotorSpeed < 0) {
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, -RightMotorSpeed);
    }
    else {
      analogWrite(RightMotorDirectionPin, 255);

      analogWrite(RightMotorSpeedPin, RightMotorSpeed);

    }
  }

  void turnLeft(int speed){
    LeftMotorSpeed = off;
    RightMotorSpeed = speed;
    if(LeftMotorSpeed < 32 && LeftMotorSpeed >-32){
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, 0);
    }
    else if (LeftMotorSpeed < 0) {
      analogWrite(LeftMotorDirectionPin, 0);

      analogWrite(LeftMotorSpeedPin, -LeftMotorSpeed);
    }
    else {
      analogWrite(LeftMotorDirectionPin, 255);

      analogWrite(LeftMotorSpeedPin, LeftMotorSpeed);

    }
 
    if(RightMotorSpeed < 32&& RightMotorSpeed >32){
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, 0);
    }
    else if (RightMotorSpeed < 0) {
      analogWrite(RightMotorDirectionPin, 0);

      analogWrite(RightMotorSpeedPin, -RightMotorSpeed);
    }
    else {
      analogWrite(RightMotorDirectionPin, 255);

      analogWrite(RightMotorSpeedPin, RightMotorSpeed);

    }
  }

void setup() {
    Serial.begin(9600);
    quit();
    stop();
    enable();
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim(); // Trim any whitespace

        if (command == "forward") {
            forward(75); // You can adjust the speed as needed
        } else if (command == "backward") {
            backward(35);
        } else if (command == "turnLeft") {
            turnLeft(35);
        } else if (command == "turnRight") {
            turnRight(35);
        } else if (command == "quit") {
            quit();
        } else if (command == "stop") {
            stop();
        }
    }
}
