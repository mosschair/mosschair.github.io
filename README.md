# mosschair.github.io

MOSSChair is dedicated to creating smart modules that can be added to a manual wheelchair so that users can make a customized wheelchair based on the wheelchair user's unique needs. So far, we have created the following modules that are controlled through code found in the code folder under our main branch. This code is put onto an NVIDIA Jetson Nano and mounted onto a manual wheelchair. 

## Our Modules
1. Motorization: we have three different motorization control modes, including key control (from a laptop), voice control, and a joystick.
2. Object Detection: through the Jetson Nano and connected camera, objects can be detected by the wheelchair.
3. Robotic Arm: a 3D-printed arm has been equipped with servo motors in the fingers and wrist area to allow for precise movement. This arm has high torque and is capable of picking up small items.


## Future Recommendations
1. Obstacle detection and avoidance: We have looked into ROS and LiDAR sensing for the wheelchair so that the wheelchair is able to drive autonomously. For future iterations of this project, we recommend looking into autonomous driving and control through LiDAR and ROS.
2. Eye movement: We recommend developing another control module for wheelchair motorization for users who have limited hand movement. We recommend looking into eye sensors and integrating these sensors with the motorization of the wheelchair so that users can move the wheelchair with their eyes.
3. Automatic weight tuning: As of now, the motors are tuned manually based on the estimated weight of the wheelchair user. We recommend eventually integrating weight sensors into the seat of the wheelchair which can help automatically tune the motor drivers of the wheelchair to ensure smooth movement of the chair, regardless of user weight.

## Things to Look Out For
1. Loose wires! Make sure that all wires are always fully connected. Even one loose wire can lead to erratic motor movement.
2. Battery charging: As of right now, we are using 2 24 V AGM batteries connected in parallel. These batteries get drained after extraneous work and need to be charged regularly.
3. Encoders: Make sure encoders are always connected to the spokes well to make sure that the motors can actually move the wheelchair.
