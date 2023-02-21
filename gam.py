import time
import random
import re


#map
w = ''
array = (40, 70)
gridX = array[1]
gridY = array[0]
#send grid to file for editing in input.py
f = open("grid.txt", "w")
f.write(str(gridX))
f.write("\n")
f.write(str(gridY))
f.close()

#player
player = 'P'
life = 3


#enemy
enemy = 'O'
enemyX = random.randint(0,5)
enemyY = random.randint(0,5)
enemy2 = 'B'
enemy2X = random.randint(5,15)
enemy2Y = random.randint(5,15)
enemy3 = '@'
enemy3X = random.randint(1,15)
enemy3Y = random.randint(1,15)

while True:

    
    #Get player position
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
        
    #track entity positions
    print("PLAYERX: ", playerX)
    print("PLAYERY: ", playerY)
    print("ENEMYX: ",enemyX)
    print("ENEMYY: ",enemyY)
    print("ENEMY2X: ",enemy2X)
    print("ENEMY2Y: ",enemy2Y)
    print("ENEMY3X: ",enemy3X)
    print("ENEMY3Y: ",enemy3Y)
    
    #Move enemy and detect collision
    if enemyX < playerX:
        print("EnemyX is behind playerX, move right")
        enemyX += 1
        print(enemyX)
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
            life -= 1
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
            else:
                w = w + "x"
        print(w)
        w = ''
    time.sleep(0.2)



