import time
import random
array = (16, 20)
gridX = array[1]
gridY = array[0]

#send grid to file for editing in input.py
f = open("grid.txt", "w")
f.write(str(gridX))
f.write("\n")
f.write(str(gridY))
f.close()

w = ''
player = 'P'
life = 3

enemy = 'O'
enemyX = random.randint(0,5)
enemyY = random.randint(0,5)

while True:
    print("GRID X: ", gridX)
    print("GRID Y: ", gridY)
    
    #Get player position
    f = open("player.txt", "r")
    playerX = f.readline()
    playerX = playerX.strip()
    playerY = f.readline()
    playerY = playerY.strip()
    playerX = int(playerX)
    playerY = int(playerY)
    
    #Set boundaries on grid
    if playerX <= 0:
        playerX += 1
    elif playerX >= gridY:
        playerX -= 2
    if playerY <= 0:
        playerY += 1
    elif playerY >= gridX:
        playerY -= 1

    print("PLAYERX: ", playerX)
    print("PLAYERY: ", playerY)
    print("ENEMYX: ",enemyX)
    print("ENEMYY: ",enemyY)

    
    #Move enemy and detect collision
    if enemyX < playerX:
        enemyX += 1
    elif enemyX == playerX:
        if enemyY == playerY:
            print("Hit. -1 life.")
            life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemyX -= 1
        
    if enemyY < playerY:
        enemyY += 1
    elif enemyY == playerY:
        if enemyX == playerX:
            print("Hit -1 life.")
            life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemyY -= 1
        
    print("Lives:",life)
    
    #Update frame
    for y in range(gridX):
        for x in range(gridY):
            if(playerX == x and playerY == y):
                w = w + player
            elif enemyX == x and enemyY == y:
                w = w + enemy
            else:
                w = w + "x"
        print(w)
        w = ''
    time.sleep(0.5)


