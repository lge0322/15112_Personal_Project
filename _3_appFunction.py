from _1_classes import *
from _2_createImage import *


################################################################################


def reset(app):
    
    createImage(app)
    app.count = 5
    app.margin = min(app.height, app.width) // 10
    app.minMargin = app.margin // 5
    app.wallList = [] #shows the location of the walls format: (x,y)
    app.coinLocation = []
    app.color = "red"
    app.status = "Closed"
    app.speed = 0
    app.gameOver = False
    app.doorOpen = False
    app.charAtDoor = False
    app.isNext = False
    app.hintButton = False
    app.timerDelay = 100

    if woodboy.die or metalgirl.die:
        app.gameOver = True

################################################################################

def charAtDoor(app):
    if app.doorOpen:
        if ((woodboy.x - app.minMargin  <= woodboy.initX <= woodboy.x + app.minMargin and
            woodboy.y - app.minMargin  <= woodboy.initY <= woodboy.y + app.minMargin) and 
            (metalgirl.x -app.minMargin  <= metalgirl.initX <= metalgirl.x + app.minMargin and 
            metalgirl.y - app.minMargin  <= metalgirl.initY <= metalgirl.y + app.minMargin)):
            app.isNext = True

################################################################################

