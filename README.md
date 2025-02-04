# Asteroids
A simple 2D Asteroids-style game built in Python using Pygame. Control a triangular ship to avoid and destroy incoming asteroids. Guided project from [boot.dev](https://boot.dev) with a few extra features / functionality. 

## Features
- Player Ship
  - Rotates using [A]/[D]
  - Moves forward/backward using [W]/[S]
  - Fires bullets using [Space]
- Asteroids
  - Spawn from screen edges
  - Split into two smaller asteroids when destroyed
- Scoring
  - Gain points for destroying asteroids
- Collisions
  - Uses circle-based collisions for the player, asteroids, and bullets
  - If an asteroid hits the player, the game ends

## Set up / Environment
- Clone the repository
```
git clone https://github.com/jw00006/AsteroidsGame.git
cd AsteroidsGame
```
- Optional: Create / use a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# or venv\Scripts\activate (Windows)
```
- Otherwise, required to install pygame through either
```
pip install -r requirements.txt
```
Or ...
```
pip install pygame 
```
Finally, running the main script
```
python3 main.py
```

![Gameplay](https://github.com/jw00006/AsteroidsGame/asteroids_gameplay.gif)

## Known Issues 
- No replay screen: Currently, the game closes on collision.
- No audio: Sound effects not yet implemented.
- No bullet cleanup: Shots fly offscreen infinitely.
- Asteroids do not reset / disappear and respawn on restart.

## Ideas for Future Improvements
- Build upon the incredibly basic scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped
