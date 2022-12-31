import module_manager
module_manager.review()

from cmu_112_graphics import *
from _1_classes import *
from _2_createImage import *
from _3_appFunction import *
from _4_0_drawEasy import *
from _4_1_drawMedium import *
from _4_2_drawHard import *
from _5_music import *

import pygame
from pygame.locals import *

###############################################################################
#initalize values

backgroundMusic()

def appStarted(app): 
    app.start = False
    app.main = False
    app.easy = False
    app.medium = False
    app.hard = False
    app.counter0 = 0
    app.counter1 = 0
    app.counter2 = 0
    app.musicCount = 0
    reset(app)

def keyPressed(app, event):
    #for starting page
    if not app.main:
        if event.key:
            app.main = True

    if app.gameOver:
        if event.key == "r":
            app.gameOver = False
            woodboy.die = False
            woodboy.x, woodboy.y = woodboy.initX, woodboy.initY
            metalgirl.x, metalgirl.y = metalgirl.initX, metalgirl.initY
            metalgirl.die = False
            woodboy.hitByWaterdrop = False
            metalgirl.hitByLightning = False
            maze0.musicCount = 0
            maze1.musicCount = 0
            maze2.musicCount = 0
            reset(app)
        
    if event.key == "Right":
        woodboy.x += woodboy.speed
    elif event.key == "Left":
        woodboy.x -= woodboy.speed
    elif event.key == "Up":
        woodboy.y -= woodboy.speed
    elif event.key == "Down":
        woodboy.y += woodboy.speed

    if event.key == "d":
        metalgirl.x += metalgirl.speed
    elif event.key == "a":
        metalgirl.x -= metalgirl.speed
    elif event.key == "w":
        metalgirl.y -= metalgirl.speed
    elif event.key == "s":
        metalgirl.y += metalgirl.speed
       
    if app.easy:
        gemEasy(app)
        if app.counter0 == sums0: 
            app.status = "Open"
            app.color = "green"
            app.doorOpen = True
            app.musicCount += 1
            if app.musicCount < 2:
                doorOpenMusic()

    elif app.medium:
        gemMedium(app)
        if app.counter1 == sums1:
            app.status = "Open"
            app.color = "green"
            app.doorOpen = True
            app.musicCount += 1
            if app.musicCount < 2:
                doorOpenMusic()
    
    elif app.hard:
        gemHard(app)
        if app.counter2 == sums2: 
            app.status = "Open"
            app.color = "green"
            app.doorOpen = True
            app.musicCount += 1
            if app.musicCount < 2:
                doorOpenMusic()

    charAtDoor(app)

def timerFired(app):
    if woodboy.die or metalgirl.die:
        app.gameOver = True
        if woodboy.hitByWaterdrop:
            app.count -= 1
            if app.count < 0:
                app.count = 0
        elif metalgirl.hitByLightning:
            app.count -= 1
            if app.count < 0:
                app.count = 0

    if ((button0.music and button0.musicCount == 5) or (button1.music and button1.musicCount == 5) 
            or (button2.music and button2.musicCount == 5)):
        buttonMusic()

    if ((switch0.music and switch0.musicCount == 5) or (switch1.music and switch1.musicCount == 5) 
            or (switch2.music and switch2.musicCount == 5)):
        switchMusic()
  
def mousePressed(app, event):
    if app.main and not app.start:
        if 100 <= event.x <= 140 and 170 <= event.y <=190:
            app.easy = True
            app.start = True
        elif 175 < event.x <= 235 and 170 <= event.y <= 190:
            app.medium = True
            app.start = True
        elif 280 < event.x <= 320 and 170 <= event.y <= 190:
            app.hard = True
            app.start = True
    else:   
        if 450 <= event.x <= 500 and 350 <= event.y <=450:
            app.hintButton = True

def redrawAll(app, canvas):
    if not app.main and not app.start:
        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow", outline = "black", width = 5)
        canvas.create_rectangle(40, 20, 390, 160, fill = "white", outline = "green")
        canvas.create_text(215, 90, text = "WOODBOY AND METALGIRL", font = "Arial 24 bold")
        canvas.create_rectangle(40, 185, 390, 215, fill = "white", outline = "green")
        canvas.create_text(200, 200, text = "Press any key to start", font = "Arial 13 bold")
        canvas.create_rectangle(40, 350, 390, 380, fill = "white", outline = "green")
        canvas.create_text(200, 365, text = "By Ella Lee", font = "Arial 13 bold")
        
    elif app.main and not app.start:
        canvas.create_text(70, 420, text = "More Information!", fill = "black", font = "Arial 12 bold")
        canvas.create_text(270, 480, text = "1. You'll probably see a lift when turning the switch.\n\n\t Whether lift appears or not depends on the level of difficulty. \n\t It basically allows coins to be generated. \n\t In other words, it is just a feature, so is for hangingwoods! \n\n 2. Obstacles are dropping at random speed, and when you move around, their speed increases \n 3. For the easy level, you don't die even if you hit the wall for the purpose of practice :)", font = "Arial 10 bold")
        canvas.create_rectangle(0, 0, 400, 400, fill = "yellow", outline = "black", width = 5)
        canvas.create_rectangle(40, 20, 390, 160, fill = "white", outline = "green")
        canvas.create_text(210, 90, text = "Instructions", font = "Arial 30 bold")
        canvas.create_rectangle(40, 210, 390, 230, fill = "white", outline = "green")
        canvas.create_text(220, 220, text= "Choose a level to start the game", font = "Arial 12 bold")
        canvas.create_rectangle(40, 230, 390, 390, fill = "white", outline = "green")
        canvas.create_text(215, 310, text = "Each game will have a randomly generated map. \n If you want to try another level or another maze on the same level \n just run the app again! \n\n Rule1: You die when colliding with the wall, \n with lightning for only Metalgirl, with waterdrops for only Woodboy \n\n Rule 2: You must collect all the coins to escape the maze. \n Press the button and collect BLUE coins \n Turn the switch right and collect GREEN coins \n Use a hint system to find the solution \n\n Rule 3: Do not move when using a hint"
                            , font = "Arial 10 bold")
        canvas.create_image(70, 150, image = app.woodboy)
        canvas.create_image(360, 150, image = app.metalgirl)
        canvas.create_rectangle(100, 170, 140, 190, fill = "white", outline = "green")
        canvas.create_rectangle(175, 170, 235, 190, fill = "white", outline = "green")
        canvas.create_rectangle(280, 170, 320, 190, fill = "white", outline = "green")
        canvas.create_text(120, 180, text = "easy", fill = "green")
        canvas.create_text(205, 180, text = "medium", fill = "blue" )
        canvas.create_text(300, 180, text = "hard", fill= "red")

    elif app.main and app.start:
        if app.easy:
            if not app.gameOver:
                drawAll0(app, canvas)
                if app.isNext:
                    canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
                    canvas.create_text(200, 200, text = "Yay! You finally escaped the maze!\n Run this app again \nto try another game", font = "Arial 23 bold")
            else:
                drawGameOver(app, canvas)
      
        elif app.medium:
            if not app.gameOver:
                drawAll(app, canvas)
                if app.isNext:
                    canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
                    canvas.create_text(200, 200, text = "Yay! You finally escaped the maze!\n Run this app again \nto try another game", font = "Arial 23 bold")
            else:
                drawGameOver(app, canvas)
        
        elif app.hard:
            if not app.gameOver:
                drawAll2(app, canvas)
                if app.isNext:
                    canvas.create_rectangle(0, 100, 400, 300, fill = "white", outline = "gray")
                    canvas.create_text(200, 200, text = "Yay! You finally escaped the maze!\n Run this app again \nto try another game", font = "Arial 23 bold")
            else:
                drawGameOver(app, canvas)

runApp(width = 550, height = 550)
        
pygame.quit()
quit()