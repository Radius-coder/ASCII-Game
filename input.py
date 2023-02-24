#input
#takes input, saves direction and stores in txt file.
#Text file is constantly check in other program to update player Posistion

from msvcrt import getch

#import grid dimensions
f = open("grid.txt", "r")
gridX = f.readline()
gridY = f.readline()
grid = (int(gridX.strip()), int(gridY))
f.close()

#import walls
wallX = []
wallY = []
f = open("walls.txt" , "r")
i = 0
while i < 50:
    line = f.readline()
    line = line.strip()
    wallX.append(int(line))
    i += 1

i=0
while i < 50:
    line = f.readline()
    line = line.strip()
    wallY.append(int(line))
    i += 1

print(wallX)
print(wallY)
print(grid)

playerX = 0
playerY = 0
x = 0
y = 0




while True:
    #track if wall hit to stop movement if hit
    wallHit = False
    i = 0
    #import player position
    f = open("player.txt", "r")
    playerX = f.readline()
    playerX = playerX.strip()
    playerY = f.readline()
    playerY = playerY.strip()
    f.close()

    print("PLAYER Position: (", playerX, ',', playerY,')')
    
    #get key press
    move = ord(getch())
    playerX = int(playerX)
    playerY = int(playerY)

    #movement and boundaries
    if(move == 119):
        print("W pressed")
        while i < len(wallX):
            if wallY[i] == playerY:
                if wallX[i] == playerX:
                    print("Wall hit")
                    playerY += 1
                    wallHit = True
                    i += 1
                else:
                    i += 1
            else:
                i += 1
                
        if wallHit == False:        
            if playerY <= 0:
                print("player too high")
                playerY += 1
            else:
                playerY -= 1
                print("Moved up")
            
    elif(move == 97):
        print("A pressed")
        while i < len(wallX):
            if wallX[i] == playerX:
                if wallY[i] == playerY:
                    print("Wall hit")
                    playerX += 1
                    wallHit = True
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        if wallHit == False:
            if playerX <= 0:
                playerX += 1
            else:
                print("moved left")
                playerX -= 1
            
    elif(move == 115):
        print("S Pressed")
        while i < len(wallX):
            if wallY[i] == playerY:
                if wallX[i] == playerX:
                    print("Wall hit")
                    playerY -= 1
                    wallHit = True
                    i += 1
                else:
                    i += 1
            else:
                i += 1
                
        if wallHit == False:
            if playerY >= int(gridY):
                print("player too low")
                playerY -= 1
            else:
                print("Moved down")
                playerY += 1
            
    elif(move == 100):
        print("D Pressed")
        while i < len(wallX):
            if wallX[i] == playerX:
                if wallY[i] == playerY:
                    print("Wall hit")
                    playerX -= 1
                    wallHit = True
                    i += 1
                else:
                    i += 1
            else:
                i += 1
                
        if wallHit == False:
            if playerX >= int(gridX):
                playerX -= 1
            else:
                print("moved right")
                playerX += 1
            
    #save player position
    f = open("player.txt", "w")
    f.write(str(playerX))
    f.write("\n")
    f.write(str(playerY))
    f.close()
    f = open("player.txt", "r")
    for x in f:
        print("Players new X coord",x)
    f.close()
