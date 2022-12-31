from _1_classes import *
from _2_createImage import *
from _3_appFunction import *
from _5_music import *

import time

################################################################################

def drawAll2(app, canvas):
    
    drawSetup(app, canvas)
    drawInstructions(app, canvas)
    draw1MazeSetup(app, canvas)
    drawCharacters(app, canvas)
    drawHint(app, canvas)
    drawLift(app, canvas)
    drawSwitch(app, canvas)
    drawCoins(app, canvas)
    hangingwood2.draw(app, canvas)
    maze2.deleteHangingWood(hangingwood2.x, hangingwood2.y)
    hangingwood3.draw(app, canvas)
    button2.draw(app, canvas)
    drawObstacleMove(app, canvas)
    
    if not len(maze2.hintList) == 0:
        canvas.create_text(470, 330, text = "you have only one hint!" , font = "Arial 12 bold", fill = "black")

    if not len(maze2.hintList) == 0 and app.hintButton:
        drawSolve(app, canvas)

################################################################################

def drawSetup(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image = app.background)
    canvas.create_rectangle(0, 0, 400, 400, fill = "yellow")
    canvas.create_text(470, 40, text = f'level 3', fill = "black", font = "Arial 15 bold")

################################################################################

def drawInstructions(app, canvas):
    #indicating # of gems to users
    canvas.create_rectangle(410, 60, 540, 300, fill = "white", outline = "yellow")
    print(maze2.counter, sums2)
    if app.counter2 == sums2:
        canvas.create_text(470, 100, text = f'All coins are \n collected!', fill = "red", font = "Arial 13 bold")
    else:
        canvas.create_text(470, 100, text = f'Currently,\n {app.counter2}\n coins \n are consumed', fill = "black", font = "Arial 13 bold")
    
    #indicating whether switches are open or not
    if switch2.isRight:
        canvas.create_text(470, 180, text = f'The switch \n has been \n open!', font = "Arial 13 bold", fill = "red")
    else:
        canvas.create_text(470, 180, text = f'Currently, \n the switch \n is not open', fill = "black", font = "Arial 13 bold")
    
    if button2.isPressed:
        canvas.create_text(470, 250, text = "The button\n has been\n pressed!", font = "Arial 13 bold", fill = "red")
    else:
        canvas.create_text(470,250, text = "The button\n has not been\n pressed.", font = "Arial 13 bold")
    
    #indicating the status of the door (whether it is open or not)
    canvas.create_text(490, 520, text = f'{app.status}', fill = app.color, font = "Arial 16 bold")

################################################################################

def drawHint(app, canvas):
    canvas.create_rectangle(420, 350, 520, 400, fill = "white", outline = "yellow")
    canvas.create_text(470, 375, text = "Show Hint", font = "Arial 12 bold")

################################################################################

def draw1MazeSetup(app, canvas):
    maze2.draw(app, canvas)
    maze2.drawDoor(app, canvas)
    maze2.isWallwithCharacter() #check if the characters are collding with the wall

################################################################################

def drawLift(app, canvas):
    min = 5
    w = maze2.w
    r = w/2 + min
    if len(maze2.liftLoc) > 1:
        for j in range(1):
            x, y = maze2.liftLoc[j][0] * w + r, maze2.liftLoc[j][1] * w
            canvas.create_image(x, y+r//5+switch2.speed, image = app.lift2)
    elif len(maze2.liftLoc) == 1:
        x, y = maze2.liftLoc[0][0] * w + r, maze2.liftLoc[0][1] * w
        canvas.create_image(x, y+r//5+switch2.speed, image = app.lift2)
        
################################################################################

def drawSwitch(app, canvas):
    switch2.draw(app, canvas)

################################################################################

def drawCharacters(app, canvas):
    canvas.create_image(woodboy.x, woodboy.y, image = app.woodboy)
    canvas.create_image(metalgirl.x, metalgirl.y, image = app.metalgirl)

################################################################################

def drawObstacleMove(app, canvas):
    lightning1.draw(app, canvas)
    lightning1.move()
    lightning1.isCharacterTouching()
    lightning2.draw(app, canvas)
    lightning2.move()
    lightning2.isCharacterTouching()
    lightning3.draw(app, canvas)
    lightning3.move()
    lightning3.isCharacterTouching()
    waterdrop1.draw(app, canvas)
    waterdrop1.move()
    waterdrop1.isCharacterTouching()
    waterdrop2.draw(app, canvas)
    waterdrop2.move()
    waterdrop2.isCharacterTouching()
    waterdrop3.draw(app, canvas)
    waterdrop3.move()
    waterdrop3.isCharacterTouching()

################################################################################

maze2.canPlaceGem()
random.shuffle(maze2.gem)
res2 = []
sums2 = 0
w=  maze2.w
r = w/2
d = r/2

#red coins
for i in range(4):
    (x, y) = maze2.gem[i][0] * w + r, maze2.gem[i][1] * w +r
    sums2+= 1
    res2.append((x, y))
    maze2.gem.remove((maze2.gem[i][0], maze2.gem[i][1]))

#green coins
resG2 = []
for i in range(4, 7):
    (x, y) = maze2.gem[i][0] * w + r, maze2.gem[i][1] * w +r
    sums2 += 1
    resG2.append((x, y))
    maze2.gem.remove((maze2.gem[i][0], maze2.gem[i][1]))

#blue coins
resB2 = []
for i in range(7, 10):
    (x, y) = maze2.gem[i][0] * w + r, maze2.gem[i][1] * w +r
    sums2 += 1
    resB2.append((x, y))

def drawCoins(app, canvas):
    for (x, y) in res2:
        canvas.create_image(x, y, image = app.coin)
    if switch2.isRight:
        for (x, y) in resB2:
            canvas.create_image(x, y, image = app.coinB)
    if button2.isPressed:
            for (x, y) in resG2:
                canvas.create_image(x, y, image = app.coinG)

################################################################################

def drawGameOver(app, canvas):
    if woodboy.die or metalgirl.die:
        canvas.create_image(app.width//2, app.height//2, image = app.background) #hardcode
        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow")
        canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
        
        if woodboy.hitByWaterdrop:
            canvas.create_text(200, 200, text = "Try again!\n Woodboy is hit by waterdrops\n Wait for 3 seconds\n Press 'r' to continue the game", font = "Arial 20 bold")
        elif metalgirl.hitByLightning:
            canvas.create_text(200, 200, text = "Try again!\n Metalgirl is hit by lightning\n  Wait for 3 seconds\nPress 'r' to continue the game", font = "Arial 20 bold")
        elif woodboy.wall or metalgirl.wall: 
            canvas.create_text(200, 200, text = "Try again!\n You cannot go through the wall\n Press 'r' to continue the game ", font = "Arial 20 bold")

################################################################################
        
def drawSolve(app, canvas):
    current = maze2.hintList.pop()
    x,y,dic = current.x, current.y, current.walls
    x = x*maze2.w
    y = y*maze2.w
    r = maze2.w//2
    midX = x + r
    midY = y + r
    d = r// 5
     
    canvas.create_rectangle(midX - d, midY-d, midX+d, midY+d, fill = "green")
    time.sleep(0.4)

################################################################################

def gemHard(app):
    #red coins
    for (x, y) in res2: 
            if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d) or 
                (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d)):
                app.counter2 += 1
                gemMusic()
                res2.remove((x,y))

    #green coins
    for (x, y) in resG2:
        if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and button2.isPressed) or 
            (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and button2.isPressed)):
            app.counter2 += 1
            gemMusic()
            resG2.remove((x,y))
            
    #blue coins
    for (x, y) in resB2:
        if ((woodboy.x - d <= x <= woodboy.x +  d and  woodboy.y - d <= y <= woodboy.y + d and switch2.isRight) or 
            (metalgirl.x - d <= x <= metalgirl.x + d and metalgirl.y - d <= y <= metalgirl.y + d and switch2.isRight)):
            app.counter2 += 1
            gemMusic()
            resB2.remove((x,y))