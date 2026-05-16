# 4-axis-robot-arm
Design and Simulation a 4Axis Robotic Arm including kinematics, CAD modelling, component selection &amp; sizing and ROS simulation.

<img width="1919" height="1357" alt="4 Axis Robot 2" src="https://github.com/user-attachments/assets/5ed18798-17e6-40bf-986c-05f0c623987e" />

This project presents the end-to-end mechanical design of a 4axis robotic arm, developed with a focus on real-world industrial applicability.
It covers kinematics, CAD modelling using SolidWorks, load estimation, and torque calculations to ensure accurate Motor, Gearbox and Driver selection.
It also includes Simulations based on Rviz & Gazebo with ROS2 for better understanding of real world pick & place applications.
The complete system is designed with attention manufacturability.
This repository documents the full engineering workflow from concept to a build-ready design.


🤖 Design Reference

The design is inspired by industrial 6-axis robotic arms such as the FANUC M-800 series.

<img width="2560" height="1712" alt="FANUC-Robot-M-800-60-20B" src="https://github.com/user-attachments/assets/63758797-0b8a-4179-b124-94debc156991" />

Instead of replicating a full 6-axis configuration, this project simplifies the architecture into a 4-axis system at a much smaller scale for ease of implementability, while preserving the key industrial motion principles:

Base rotation for workspace coverage
Shoulder and Elbow articulation for reach and load handling
Wrist/End-effector orientation control

This reduction in degrees of freedom was intentionally done to:

Simplify mechanical design and control complexity
Focus on core kinematics and load handling principles
Make the system more accessible for industrial motion behavior in simulation
