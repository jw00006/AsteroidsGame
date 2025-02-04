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

## Known Issues / Future Improvements
- No replay screen: Currently, the game closes on collision.
- No audio: Sound effects not yet implemented.
- No bullet cleanup: Shots fly offscreen infinitely.
