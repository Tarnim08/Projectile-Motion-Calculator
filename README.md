# Python-Based Projectile Motion Calculator

## About the Project

This is a simple Python programme that calculates different values related to projectile motion.

I created this project to combine my knowledge of A-level Physics with my interest in Python programming.

## Features

The programme calculates:

- Time of flight
- Maximum height
- Horizontal range

It takes the initial velocity and angle of projection as inputs from the user.

## Physics Equations Used

The programme uses the following equations:

**Time of flight:**

T = (2u sin θ) / g

**Maximum height:**

H = (u² sin² θ) / (2g)

**Horizontal range:**

R = (u² sin 2θ) / g

Where:

- u = Initial velocity
- θ = Angle of projection
- g = Gravitational acceleration (9.81 m/s²)

## Technologies Used

- Python
- Python math library

## Requirements

- Python 3 installed on your computer.

No external libraries are required for the basic calculator.

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the following command in your terminal:

`python projectile_calculator.py`

4. Enter the initial velocity and angle when requested.
5. View the calculated results.

## Example

**Input:**
- Initial velocity: 20 m/s
- Projection angle: 45°

**Output:**
- Time of flight: 2.88 seconds
- Maximum height: 10.19 metres
- Horizontal range: 40.77 metres

## Assumptions and Limitations

- Air resistance is ignored.
- Gravitational acceleration is assumed to be 9.81 m/s².
- The projectile lands at the same height from which it was launched.

## Future Improvements

- Add a graph showing the projectile's trajectory.
- Add support for different launch and landing heights.
- Include the effect of air resistance.

## Author

Tarnim Ahmed

Independent Programming Project
