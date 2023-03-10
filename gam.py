import time
import random
import re


#map
w = ''
gridX = int(input("Enter the max value on the X axis: "))
gridY = int(input("Enter the max value on the Y axis: "))
print("loading grid...")
array = (gridY, gridX)
#send grid to file for editing in input.py
f = open("grid.txt", "w")
f.write(str(gridX))
f.write("\n")
f.write(str(gridY))
f.close()


#walls
f = open("walls.txt", "w")
f.write('')
f.close()

wall = '□'
wallX = []
wallY = []

i = 0
while i < 50:
    f = open("walls.txt", "a")
    x = random.randint(0,gridX)
    wallX.append(x)
    f.write(str(x))
    f.write("\n")
    i += 1
    f.close()
    
i = 0
while i < 50:
    f = open("walls.txt", "a")
    y = random.randint(0, gridY)
    wallY.append(y)
    f.write(str(y))
    f.write("\n")
    i += 1
    f.close()



#player
player = 'P'
life = 3
#reset player position
f = open("player.txt", "w")
f.write('0')
f.write("\n")
f.write('0')
f.close()
print("loading player...")
#enemy
enemy = 'O'
enemyX = random.randint(0,gridX)
enemyY = random.randint(0,gridY)
enemy2 = 'B'
enemy2X = random.randint(5,gridX)
enemy2Y = random.randint(5,gridY)
enemy3 = '@'
enemy3X = random.randint(1,gridX)
enemy3Y = random.randint(1,gridY)
print("loading enemies...")
print("loading walls...")

print("WALLX: ", wallX)
print("WALLY: ", wallY)

print("Starting in 3...")
time.sleep(1)
print("Starting in 2...")
time.sleep(1)
print("Starting in 1...")
time.sleep(1)
print("GO!")
time.sleep(1)
while True:
    #Get/Set player position
    f = open("player.txt", "r")
    playerX = f.readline()
    playerX = playerX.strip()
    playerX = playerX.replace(' ', '')
    playerY = f.readline()
    playerY = playerY.strip()
    playerY = playerY.replace(' ', '')
    print("B4 turning to int", playerX)
    if playerX == "":
        playerX = tempPlayerX
    else:
        playerX = int(playerX)
    print("After:", playerX)
    print("B4 turning to int", playerY)
    if playerY == "":
        playerY = tempPlayerY
    else:
        playerY = int(playerY)
        
    print("AFTER: ", playerY)
    f.close()

    '''Sometimes player position is read as blank (unsure why atm, must be input.py)
    so this should store the last valid value in case it becomes blank'''
    tempPlayerX = playerX
    tempPlayerY = playerY
    
    #Set boundaries on grid
    if playerX <= 0:
        playerX += 1
    elif playerX >= gridY:
        playerX -= 2
    if playerY <= 0:
        playerY += 1
    elif playerY >= gridX:
        playerY -= 1
        
    #Track entity positions
    print("PLAYER POSITION: (",playerX,', ',playerY,")")
    print("ENEMY 1 POSITION: (",enemyX,', ' ,enemyY,")")
    print("ENEMY 2 POSITION: (",enemy2X,', ' ,enemy2Y,")")
    print("ENEMY 3 POSITION: (",enemy3X,', ' ,enemy3Y,")")

    
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



    #Move enemy2 and detect collision
    if enemy2X < playerX:
        enemy2X += 1
    elif enemy2X == playerX:
        if enemy2Y == playerY:
            print("Hit. -1 life.")
            life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemy2X -= 1
        
    if enemy2Y < playerY:
        enemy2Y += 1
    elif enemy2Y == playerY:
        if enemy2X == playerX:
            print("Hit -1 life.")
            life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemy2Y -= 1


    #Move enemy3 and detect collision
    if enemy3X < playerX:
        enemy3X += 1
    elif enemy3X == playerX:
        if enemy3Y == playerY:
            print("Hit. -1 life.")
            #life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemy3X -= 1
        
    if enemy3Y < playerY:
        enemy3Y += 1
    elif enemy3Y == playerY:
        if enemy3X == playerX:
            print("Hit -1 life.")
            life -= 1
            if life <= 0:
                print("GAME OVER!")
                break
    else:
        enemy3Y -= 1
        
    print("Lives:",life)
    
    #Enemy colliding with each other
    if enemyX == enemy2X or enemyX == enemy3X:
        if enemyY == enemy2Y or enemyY == enemy3Y:
            enemyX -= 1
            enemyY -= 1
    elif enemy2X == enemyX or enemy2X == enemy3X:
        if enemy2Y == enemyY or enemy2Y == enemy3Y:
            enemy2X += 1
            enemy2Y += 1
    elif enemy3X == enemyX or enemy3X == enemy2X:
        if enemy3Y == enemyY or enemy3Y == enemy2Y:
           enemy3X -= 2
           enemy3Y -= 2


    #Enemy colliding with walls (needs changing)
        if enemyX in wallX:
            if enemyY in wallY:
                print("Enemy colliding with wall")
                enemyX -= 1
                enemyY -= 1
        elif enemy2X in wallX:
            if enemy2Y in wallY:
                print("Enemy2 colliding with wall")
                enemy2X += 1
                enemy2Y += 1
        elif enemy3X in wallX:
            if enemy3Y in wallY:
                print("Enemy3 colliding with wall")
                enemy3X -= 2
                enemy3Y -= 2

    
    #Update frame
    for y in range(gridY):
        for x in range(gridX):
            if(playerX == x and playerY == y):
                w = w + player
            elif enemyX == x and enemyY == y:
                w = w + enemy
            elif enemy2X == x and enemy2Y == y:
                w = w + enemy2
            elif enemy3X == x and enemy3Y == y:
                w = w + enemy3
            else: #if not enemy or player then its wall or normal piece
                i = 0
                while i < len(wallX):
                    #if current grid Y is the same as the wallY
                    if wallY[i] == y:
                        #And the current grid X is the same as the wallX
                        if x == wallX[i]:
                            w = w + wall
                            i = 50
                        else: #if not matching wallX 
                            i += 1
                            #no wall in current gridX
                            if i == 50:
                                w = w + ' '
                    else:
                        #no wall in current grid x and y
                        i += 1
                        if i == 50:
                            w = w + ' '
        print(w)
        w = ''
    #Time is framerate (0.5 = half a second)
    time.sleep(0.3)



