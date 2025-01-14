# Air Hockey with Particle Systems

A physics-based air hockey game featuring dynamic particle systems and real-time collision detection, built using Python and PyGame. This project includes a regular version of the game, an option for a trail effect, a fire effect, and a smoke effect. 

## Overview
This air hockey simulation combines classic gameplay with modern visual effects:
- Realistic puck physics and paddle collisions 
- Dynamic particle trails and collision effects
- Smooth paddle movement and controls
- Score tracking and game state management

## Technical Features
- Custom particle system for visual effects
 - Collision-based particle generation
 - Particle lifetime management
 - Dynamic color and blending
   
- Physics Implementation
 - Velocity-based movement
 - Law of Reflection used 
 - Elastic collision detection
 - Boundary checking


## Controls
- Player 1: WASD keys
- Player 2: IJKL keys
- R: Reset game
- ESC: Exit game
- SPACEBAR: Starts the game
- 0: No particle emissions
- 1: Simple particle emissions
- 2: Complex particle emissions
- 3: Another complex emission

## Implementation Details
- Built with Python and PyGame
- Vector mathematics for physics calculations
- Real-time particle rendering
- Score and state management system


## Building and Running
1. Verify that the smoke.png image is in your directory.
2. Run the program from airhockey_main.py
3. Install required packages:
```python
pip install pygame
