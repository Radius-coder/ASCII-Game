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

print(grid)

playerX = 0
playerY = 0
x = 0
y = 0


while True:
    #import player position
    f = open("player.txt", "r")
    playerX = f.readline()
    playerX = playerX.strip()
    playerY = f.readline()
    playerY = playerY.strip()
    f.close()

    print("PLAYERX:", playerX)
    print("PLAYERY: ", playerY)

    #get key press
    move = ord(getch())
    print(move)
    playerX = int(playerX)
    playerY = int(playerY)

    #movement and boundaries
    if(move == 119):
        if playerY <= 0:
            print("player too high")
            playerY += 1
        else:
            playerY -= 1
    elif(move == 97):
        if playerX <= 0:
            playerX += 1
        else:
            playerX -= 1
    elif(move == 115):
        if playerY >= int(gridY):
            print("player too low")
            playerY -= 1
        else:
            playerY += 1
    elif(move == 100):
        if playerX >= int(gridX):
            playerX -= 1
        else:
            playerX += 1
            
    #save player position
    f = open("player.txt", "w")
    f.write(str(playerX))
    f.write("\n")
    f.write(str(playerY))
    f.close()
    f = open("player.txt", "r")
    for x in f:
        print("new",x)
    f.close()
