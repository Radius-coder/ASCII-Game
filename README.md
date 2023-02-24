# ASCII-Game
This project uses text to create a 2d game. So far I have created a 2d grid that includes a player (P) and 3 enemies (O, B, @). The player can move around while the enemies chase them. There are also walls (□). The player cannot go through walls.

<img width="960" alt="Untitled" src="https://user-images.githubusercontent.com/67561957/221177847-23be14b3-d978-495c-ab32-00bda88491af.png">

On the left you can see 'input.py'. This program is tracking and moving the player's location. It does this using 'getch' which reads keyboard inputs. The input is translated into a movement and the new position is saved to a text file.

On the right you can see 'gam.py' This program updates the enemy and player positions on to the grid. It gets the player position by reading the text file created by 'input.py' and using that position to update the board. I have done it this way so the player can move without pressing enter after each movement and the board can update even when the player does not move.

## To run
First, run gam.py. This program shows the grid, player and enemy. The enemy position is updated here. Select your grid size and when its loaded go to second program.

Secondly, run input.py. This program takes the movement inputs and updates gam.py without the need for the user to press enter after every input. This program will only launch without error once gam.py has created a board with walls and enemies.

## Features
Move player with WASD.

Enemies moves towards player position.

Player has 3 lives. They lose one life when the enemy is in the same position.

Game ends when player has 0 lives.

## To be added
Let player select amount of walls or, base wall count on grid size.

Adding projectiles the player can shoot or has to avoid.

Need to add collision between enemies and walls.

Need to test and fix player collisions with walls.

Need to fix outputs on 'input.py' so things are more clear

Adding multiple levels. - This will be done by checking when the user goes past the X coordinate of the grid. At that point a new grid is generated to represent a new level.

## Changlog
### Update 0.4
Fixed walls so they spawn in correctly.

Fixed collision with walls, however still needs improved as player can walk into wall before being sent back.

Changed board spaces from an 'x' to a blank space.

### Update 0.3
Added Walls and player collision with walls

Added option for player to change grid size.

### Update 0.2
Added 2 new enemies and their collision.

Fixed grid dimensions.

Added grid boundaries to stop the player leaving the player field.
