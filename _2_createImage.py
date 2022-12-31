from cmu_112_graphics import *
from _1_classes import *

def createImage(app):

    backgroundImage = app.loadImage("backgroundImage.jpg")
    backgroundImage = app.scaleImage(backgroundImage, 1.3)
    app.background = ImageTk.PhotoImage(backgroundImage)

    doorImage0 = app.loadImage("DoorClosed.png")
    doorImage0 = app.scaleImage(doorImage0, 0.25)
    app.door0 = ImageTk.PhotoImage(doorImage0)

    doorImage = app.loadImage("DoorClosed.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.door = ImageTk.PhotoImage(doorImage)

    doorImage2 = app.loadImage("DoorClosed.png")
    doorImage2 = app.scaleImage(doorImage2, 0.18)
    app.door2 = ImageTk.PhotoImage(doorImage2)
    
    doorImage0 = app.loadImage("MetalgirlDoorOpen.png")
    doorImage0 = app.scaleImage(doorImage0, 0.25)
    app.doorM0 = ImageTk.PhotoImage(doorImage0)

    doorImage = app.loadImage("MetalgirlDoorOpen.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.doorM = ImageTk.PhotoImage(doorImage)

    doorImage2 = app.loadImage("MetalgirlDoorOpen.png")
    doorImage2 = app.scaleImage(doorImage2, 0.20)
    app.doorM2 = ImageTk.PhotoImage(doorImage2)

    doorImage0 = app.loadImage("WoodboyDoorOpen.png")
    doorImage0 = app.scaleImage(doorImage0, 0.25)
    app.doorW0 = ImageTk.PhotoImage(doorImage0)

    doorImage = app.loadImage("WoodboyDoorOpen.png")
    doorImage = app.scaleImage(doorImage, 0.2)
    app.doorW = ImageTk.PhotoImage(doorImage)

    doorImage2 = app.loadImage("WoodboyDoorOpen.png")
    doorImage2 = app.scaleImage(doorImage2, 0.18)
    app.doorW2 = ImageTk.PhotoImage(doorImage2)

    woodboyImage = app.loadImage("Woodboy.png")
    woodboyImage = app.scaleImage(woodboyImage, 0.08)
    app.woodboy = ImageTk.PhotoImage(woodboyImage)

    metalgirlImage = app.loadImage("Metalgirl.png")
    metalgirlImage = app.scaleImage(metalgirlImage, 0.08)
    app.metalgirl = ImageTk.PhotoImage(metalgirlImage)

    woodboyImage0 = app.loadImage("Woodboy.png")
    woodboyImage0 = app.scaleImage(woodboyImage0, 0.1)
    app.woodboy0 = ImageTk.PhotoImage(woodboyImage0)

    metalgirlImage0 = app.loadImage("Metalgirl.png")
    metalgirlImage0 = app.scaleImage(metalgirlImage0, 0.1)
    app.metalgirl0 = ImageTk.PhotoImage(metalgirlImage0)

    switchLeftImage = app.loadImage("SwitchLeft.png")
    switchLeftImage = app.scaleImage(switchLeftImage, 0.08)
    app.switchLeft = ImageTk.PhotoImage(switchLeftImage)

    switchRightImage = app.loadImage("SwitchRight.png")
    switchRightImage = app.scaleImage(switchRightImage, 0.08)
    app.switchRight = ImageTk.PhotoImage(switchRightImage)

    switchLeftImage0 = app.loadImage("SwitchLeft.png")
    switchLeftImage0 = app.scaleImage(switchLeftImage0, 0.1)
    app.switchLeft0 = ImageTk.PhotoImage(switchLeftImage0)

    switchRightImage0 = app.loadImage("SwitchRight.png")
    switchRightImage0 = app.scaleImage(switchRightImage0, 0.1)
    app.switchRight0 = ImageTk.PhotoImage(switchRightImage0)

    switchLeftImage2 = app.loadImage("SwitchLeft.png")
    switchLeftImage2 = app.scaleImage(switchLeftImage2, 0.075)
    app.switchLeft2 = ImageTk.PhotoImage(switchLeftImage2)

    switchRightImage2 = app.loadImage("SwitchRight.png")
    switchRightImage2 = app.scaleImage(switchRightImage2, 0.075)
    app.switchRight2 = ImageTk.PhotoImage(switchRightImage2)

    buttonImage = app.loadImage("Button.png")
    buttonImage = app.scaleImage(buttonImage, 0.11)
    app.button = ImageTk.PhotoImage(buttonImage)

    buttonImage0 = app.loadImage("Button.png")
    buttonImage0 = app.scaleImage(buttonImage0, 0.13)
    app.button0 = ImageTk.PhotoImage(buttonImage0)

    buttonImage2 = app.loadImage("Button.png")
    buttonImage2 = app.scaleImage(buttonImage2, 0.1)
    app.button2 = ImageTk.PhotoImage(buttonImage2)

    buttonPressedImage = app.loadImage("ButtonPressed.png")
    buttonPressedImage = app.scaleImage(buttonPressedImage, 0.06)
    app.buttonPressed = ImageTk.PhotoImage(buttonPressedImage)

    buttonPressedImage0 = app.loadImage("ButtonPressed.png")
    buttonPressedImage0 = app.scaleImage(buttonPressedImage0, 0.08)
    app.buttonPressed0 = ImageTk.PhotoImage(buttonPressedImage0)

    waterdropImage = app.loadImage("Waterdrop.png")
    waterdropImage = app.scaleImage(waterdropImage, 0.03)
    app.waterdrop = ImageTk.PhotoImage(waterdropImage)

    lightning1Image = app.loadImage("Lightning1.png")
    lightning1Image = app.scaleImage(lightning1Image, 0.03)
    app.lightning1 = ImageTk.PhotoImage(lightning1Image)

    lightning2Image = app.loadImage("Lightning2.png")
    lightning2Image = app.scaleImage(lightning2Image, 0.03)
    app.lightning2 = ImageTk.PhotoImage(lightning2Image)

    lightning3Image = app.loadImage("Lightning3.png")
    lightning3Image = app.scaleImage(lightning3Image, 0.03)
    app.lightning3 = ImageTk.PhotoImage(lightning3Image)

    liftImage = app.loadImage("Lift.png")
    liftImage = app.scaleImage(liftImage, 0.055) 
    app.lift = ImageTk.PhotoImage(liftImage)

    liftImage2 = app.loadImage("Lift.png")
    liftImage2 = app.scaleImage(liftImage2, 0.045) 
    app.lift2 = ImageTk.PhotoImage(liftImage2)

    hangingWoodImage = app.loadImage("HangingWood.png")
    hangingWoodImage = app.scaleImage(hangingWoodImage, 0.15)
    app.hangingWood = ImageTk.PhotoImage(hangingWoodImage)

    coinGImage = app.loadImage("coinG.png")
    coinGImage = app.scaleImage(coinGImage, 0.05)
    app.coinG = ImageTk.PhotoImage(coinGImage)

    coinBImage = app.loadImage("coinB.png")
    coinBImage = app.scaleImage(coinBImage, 0.05)
    app.coinB = ImageTk.PhotoImage(coinBImage)

    coinImage = app.loadImage("Coin.png")
    coinImage = app.scaleImage(coinImage, 0.05)
    app.coin = ImageTk.PhotoImage(coinImage)