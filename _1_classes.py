import random
from _5_music import *

################################################################################

#Cited: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
#Cited: https://favtutor.com/blogs/breadth-first-search-python

################################################################################

class Square:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pairs = {'T': 'B', 'B': 'T', 'L': 'R', 'R': 'L'} #complements
        self.walls = {'T': True, 'B': True, 'L': True, 'R': True} #intialize all the dirs to have walls

    def need_to_go_through_walls(self):
        for key in self.walls:
            if not self.walls[key]:
                return False
        return True #see if a cell has all walls

    def highlight(self, app, canvas):
        x, y = self.x * maze1.w, self.y * maze1.w
        canvas.create_rectangle(x+10, y+10, x+maze1.w-10, x+maze1.w-10, fill = "green", outline = "white" )

################################################################################

class Maze:

    def __init__(self, rows, cols, level, i=0, j=0):
        self.rows, self.cols = rows, cols
        self.grid = self.rows * self.cols
        self.level = level
        self.i, self.j = i, j #initial position
        self.board = [[Square(row, col) for col in range(cols)] for row in range(rows)] #giving the cell a location in the list
        self.top = self.bottom = self.right = self.left = 0
        self.wallListX = []
        self.wallListY = []
        self.hintList = []
        self.gem = []
        self.coinList = []
        self.coinConsumed = []
        self.liftLoc = []
        self.lift = True
        self.speed = 5
        self.w = 400 // rows
        self.counter = 0
        self.musicCount = 0

    def isNextValid(self, cell):
        res = []
        for dir, (dx, dy) in [('T', (0, -1)), ('B', (0, 1)), ('R', (1, 0)), ('L', (-1, 0))]:
            newX, newY = cell.x + dx, cell.y + dy
            if self.isLegal(newX, newY):
                if self.board[newX][newY].need_to_go_through_walls(): #needs to go through this wall
                    res.append((dir, self.board[newX][newY]))
        return res
    
    def isLegal(self, x, y):
        if 0 <= x < self.rows and (0 <= y < self.cols):
            return True
        return False

    def make_maze(self):
        res = []
        curBlock = self.board[self.i][self.j] 
        visited = 1 

        while visited < self.grid: #until all the cells are visited 
            if not self.isNextValid(curBlock):
                i = -1
                curBlock = res[i]
                res.pop(i)
                continue

            res.append(curBlock) 
            self.hintList.append(curBlock)
            dir, nextBlock = random.choice(self.isNextValid(curBlock)) #this is a core of random board generation

            #remove the wall at the block
            curBlock.walls[dir] = False
            nextBlock.walls[curBlock.pairs[dir]] = False
            visited += 1
            curBlock = nextBlock

    def getWallPos(self):
        for row in self.board:
            for col in row:
                x, y, dic = col.x, col.y, col.walls
                w = self.w
                r = self.w/2
                y = y * w
                x = x * w
                midX = x + r
                midY = y + r

                for val in dic: #val = dirs
                    if dic[val]: #when walls exist
                        if val == "T":
                            self.wallListX.append((x, x+w, y)) #top
                        elif val == "B":
                            self.wallListX.append((x, x+w, midY+r))
                        elif val == "R":
                            self.wallListY.append((y, y+w, midX+r))
                        elif val == "L":
                            self.wallListY.append((y, y+w, x))
                        
    #find locations for the lift ("N" of two or three columns should be False)
    def canBeLift(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols-3):
                #here, y is col, which is an actual x for tkinter. Same for x (row)
                i, j, k= self.board[x][y+1].walls["T"], self.board[x][y+2].walls["T"],self.board[x][y+3].walls["T"]
                if (not i and not j and not k) or (not i and not j and k): #the entire two rows should be empty
                    res.append((x,y+1)) 
        
        #if there are no such cells, just return None, as lifts are unnecessary for that stage
        if len(res) == 0:
            self.lift = False #checking if there's any possible location
        else:
            self.liftLoc = res

        return res
       
    '''
    Conditions for switches:
        1. the ground ("B") should be present
        2. they cannot be on the initial locations of the characters
        3. they cannot be on the same locations with lift
        4. they cannot be on the same locations with buttons
            - more specifically, not on the same row and not on the same col
        5. the number of the switches are equal to the number of the lifts 
        (as they operate the lifts)

    '''
    def canBeSwitch(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                if ((x, y) == (0, 0) or (x, y) == (self.rows-1, self.cols-1) 
                        or (x, y) in self.canBeLift()): #2nd cond & 3rd cond
                    continue
                for key in self.board[x][y].walls:
                    if key == "B" and self.board[x][y].walls[key]: #1st cond
                            res.append((x, y))
        return res

    def canPlaceButton(self): #4th cond
        res = []
        if self.level == "easy":
            for val in self.canBeSwitch():
                if not ((val[0] == switch0.x and val[1] == switch0.y) or 
                        (val[0] == switch0.x and val[1] != switch0.y)
                        or (val[0] != switch0.x and val[1] == switch0.y)):
                    res.append(val)

        elif self.level == "medium":
            for val in self.canBeSwitch():
                if not ((val[0] == switch1.x and val[1] == switch1.y) or 
                        (val[0] == switch1.x and val[1] != switch1.y)
                        or (val[0] != switch1.x and val[1] == switch1.y)):
                    res.append(val)

        elif self.level == "hard":
            for val in self.canBeSwitch():
                if not ((val[0] == switch2.x and val[1] == switch2.y) or 
                        (val[0] == switch2.x and val[1] != switch2.y)
                        or (val[0] != switch2.x and val[1] == switch2.y)):
                    res.append(val)
        if len(res) == 0:
            return [(-1, -1)]

        return res

    '''
    For hanging wood, if "N" and "B" of a cell are False (does not have a cell), 
    the condition is met.

    Exception: also avoid locations of the lift (since their conditions are somewhat similiar)
    '''
    def canBeHangingWood(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols-1):
                if ((x, y) == (0, 0) or (x, y) == (self.rows-1, self.cols-1)):
                    continue
                if self.lift and (x, y+1) in self.canBeLift(): #exception
                        continue
                if self.board[x][y].walls["T"] and not self.board[x][y].walls["B"]:
                    res.append((x,y))
        if res == 0:
            return [(-1, -1) for i in range(5)]
        return res

    def deleteHangingWood(self, x, y):
        self.canBeHangingWood().remove((x,y))

    def canPlaceGem(self):
        res = []
        for x in range(self.rows):
            for y in range(self.cols):
                if (((x, y) == (0, 0) or 
                    (x, y) == (self.rows-1, self.cols-1))):
                    continue
                res.append((x, y))
        
        self.gem = res
        return res

    def isWallwithCharacter(self):
        for (x1, x2, y) in self.wallListX:
            if x1<= woodboy.x <= x2 and woodboy.y == y:
                    woodboy.wall = True
                    woodboy.die = True
                    self.musicCount += 1
                    if self.musicCount < 2:
                        dieMusic()
            if x1<= metalgirl.x <= x2 and metalgirl.y == y:
                    metalgirl.wall = True
                    metalgirl.die = True
                    self.musicCount += 1
                    if self.musicCount < 2:
                        dieMusic()
                
        for (y1, y2, x) in self.wallListY:
            if y1 <= woodboy.y <= y2 and woodboy.x == x:
                woodboy.wall = True
                woodboy.die = True
                self.musicCount += 1
                if self.musicCount < 2:
                        dieMusic()
            if y1 <= metalgirl.y <= y2 and metalgirl.x == x:
                metalgirl.wall = True
                metalgirl.die = True
                self.musicCount += 1
                if self.musicCount < 2:
                        dieMusic()

# draw the maze!

    def draw(self, app, canvas):
        for row in self.board:
            for col in row:
                x, y, dic = col.x, col.y, col.walls
                w = self.w
                r = w/2
                y = y * w 
                x = x* w 
                midX = x + r
                midY = y + r
                self.top = canvas.create_line(x, y, x+w, y, fill= "black", width = 7)
                self.bottom = canvas.create_line(x, midY+r, x+w, midY+r, fill = "black", width = 7)
                self.right = canvas.create_line(midX+r, y, midX+r, y+w, fill = "black", width = 7)
                self.left = canvas.create_line(x, y, x, y+w, fill = "black", width = 7)
                self.wallListX.append((x, x+w, y))
                self.wallListX.append((x, x+w, midY+r))
                self.wallListY.append((y, y+w, midX+r))
                self.wallListY.append((y, y+w, x))

                for val in dic:
                    if not dic[val]:
                        if val == "T":
                            canvas.delete(self.top)
                            self.wallListX.remove((x, x+w, y))

                        if val == "B":
                            canvas.delete(self.bottom)
                            self.wallListX.remove((x, x+w, midY+r))
                            
                        if val == "R":
                            canvas.delete(self.right)
                            self.wallListY.remove((y, y+w, midX+r))

                        if val == "L":
                            canvas.delete(self.left)
                            self.wallListY.remove((y, y+w, x))

    def drawDoor(self, app, canvas): #fixed location
        min = 10
        if app.doorOpen:
            if self.level =="easy":
                canvas.create_image(app.margin, app.margin, image = app.doorW)
                canvas.create_image(350, 350, image = app.doorM)

            elif self.level == "medium":
                canvas.create_image(app.margin, app.margin, image = app.doorW)
                canvas.create_image(350, 350, image = app.doorM)

            elif self.level == "hard":
                canvas.create_image(app.margin - min, app.margin - min, image = app.doorW2)
                canvas.create_image(350, 350, image = app.doorM2)
        
        else:
            if self.level =="easy":
                canvas.create_image(app.margin + min, app.margin + min, image = app.door0)
                canvas.create_image(350 - min, 350 - min, image = app.door0)

            elif self.level == "medium":
                canvas.create_image(app.margin, app.margin, image = app.door)
                canvas.create_image(350, 350, image = app.door)

            elif self.level == "hard":
                canvas.create_image(app.margin - min * 2, app.margin - min, image = app.door2)
                canvas.create_image(350 + min, 350 + min, image = app.door2)
        
################################################################################

maze0 = Maze(3, 3, "easy", 0, 0)
maze1 = Maze(4, 4, "medium", 0, 0)
maze2 = Maze(5, 5, "hard", 0, 0)

maze0.make_maze()
maze0.getWallPos()
maze1.make_maze()
maze1.getWallPos()
maze2.make_maze()
maze2.getWallPos()

################################################################################

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initX = x
        self.initY = y
        self.speed = 10
        self.hitByLightning = False
        self.hitByWaterdrop = False
        self.wall = False
        self.die = False # check if characters touched the wall or obstacles

################################################################################

woodboy = Character(50, 50)  #fixed characters' position 
metalgirl = Character(350, 350) 

################################################################################

class Switch(Maze):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        if level == "easy":
            self.x, self.y = random.choice(maze0.canBeSwitch())
            self.w = maze0.w
        elif level == "medium":
            self.x, self.y = random.choice(maze1.canBeSwitch())
            self.w = maze1.w
        elif level == "hard":
            self.x, self.y = random.choice(maze2.canBeSwitch())
            self.w = maze2.w

        self.isRight = False
        self.music = False
        self.pos = []
        self.speed = 0
        self.musicCount = 0
        
        if self.level == "easy" or self.level == "medium":
            self.maxSpeed = 140
        elif self.level == "hard":
            self.maxSpeed = 160
        
    def draw(self, app, canvas):
        w = self.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w
        self.pos.append((self.x, self.y))

        if ((x<= metalgirl.x <= x+r and y<= metalgirl.y <= y+r) or
                (x<= woodboy.x <= x+r and y<= woodboy.y <= y+r)):
       
            self.isRight = True
            self.isTouched = True
            self.music = True
            self.move()

            if self.level == "easy":
                canvas.create_image(x+r, y+w-d/1.5, image = app.switchRight0)
            elif self.level == "medium":
                canvas.create_image(x+r, y+w-d, image = app.switchRight)
            else:
                canvas.create_image(x+r, y+w-d, image = app.switchRight2)
            
            self.musicCount += 1

            if self.musicCount > 40:
                self.musicCount = 0

        else:
            self.isRight = False
            self.music = False

            if self.level == "easy":
                canvas.create_image(x+r, y+w-d/1.5, image = app.switchLeft0)
            elif self.level == "medium":
                canvas.create_image(x+r, y+w-d, image = app.switchLeft)
            else:
                canvas.create_image(x+r, y+w-d, image = app.switchLeft2)
            
    def move(self):
        if self.isRight:
            self.speed += 15
            if self.speed > self.maxSpeed:
                self.speed -= 15
################################################################################

switch0 = Switch("switch", "easy")
switch1 = Switch("switch", "medium")
switch2 = Switch("swtich", "hard")

################################################################################

class HangingWood(Maze):
    def __init__(self, name, level):
        self.name = name 
        self.level = level
        if level == "easy":
            self.x, self.y = random.choice(maze0.canBeHangingWood())
            self.w = maze0.w
        elif level == "medium":
            self.x, self.y = random.choice(maze1.canBeHangingWood())
            self.w = maze1.w
        elif level == "hard":
            self.x, self.y = random.choice(maze2.canBeHangingWood())
            self.w = maze2.w

    def draw(self, app, canvas):
        w = self.w
        r = self.w/2
        min = 10

        if self.level == "medium":
            canvas.create_image(self.x * w + r, self.y * w + r, image = app.hangingWood)
        elif self.level == "hard":
            canvas.create_image(self.x * w + r, self.y * w + r + min, image = app.hangingWood)

################################################################################

hangingwood0 = HangingWood("hangingwood0", "easy")
hangingwood1 = HangingWood("hangingwood1", "medium")
hangingwood2 = HangingWood("hangingwood2", "hard")
hangingwood3 = HangingWood("hangingwood2", "hard")

################################################################################

class Button(Maze):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        if level == "easy":
            self.x, self.y = random.choice(maze0.canPlaceButton())
            self.w = maze0.w
        elif level == "medium":
            self.x, self.y = random.choice(maze1.canPlaceButton())
            self.w = maze1.w
        elif level == "hard":
            self.x, self.y = random.choice(maze2.canPlaceButton())
            self.w = maze2.w
        self.isPressed = False
        self.music = False
        self.musicCount = 0
   
    def draw(self, app, canvas):
        w = self.w
        r = w/2
        d = w/5
        x = self.x * w
        y = self.y * w
        
        if ((x<= metalgirl.x <= x+r and y+d<= metalgirl.y <= y+r) or
                (x <= woodboy.x <= x+r and y+d<= woodboy.y <= y+r)):
            if self.level == "easy":
                canvas.create_image(x+r, y+w-d, image = app.buttonPressed0)
            elif self.level == "medium":
                canvas.create_image(x+r, y+w-d/3, image = app.buttonPressed)
            else:
                canvas.create_image(x+r, y+w-d, image = app.buttonPressed)

            self.isPressed = True
            self.music = True
            self.musicCount += 1

            if self.musicCount > 50:
                self.musicCount = 0
        
        else:
            if self.level == "easy":
                canvas.create_image(x+r, y+w-d/1.5, image = app.button0)
            elif self.level == "medium":
                canvas.create_image(x+r, y+w-d/1.5, image = app.button)
            else:
                canvas.create_image(x+r, y+w-d, image = app.button2)

            self.music = False
            self.isPressed = False

################################################################################

button0 = Button("button", "easy")
button1 = Button("button", "medium")
button2 = Button("button2", "hard")

################################################################################

class Obstacles:
    def __init__(self, x, y, name, type):
        self.x, self.y = x, y #random depending on the width, height of the platfrom (hardcoding)
        self.name = name
        self.speed = 0
        self.type = type
        self.w = maze1.w
        self.musicCount = 0

    def draw(self, app, canvas):
        w = 100
        if self.name == "lightning1":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning1)
        elif self.name == "lightning2":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning2)
        elif self.name == "lightning3":
            canvas.create_image(self.x, self.y + self.speed, image = app.lightning3)
        elif self.type == "waterdrop":
            canvas.create_image(self.x, self.y + self.speed, image = app.waterdrop)
    
    def move(self):
        self.speed = random.randint(5, 9)
        self.y += self.speed
        if self.y >= 400: #hardcode
            self.y = 0

    def isCharacterTouching(self):
        min = 20
        if self.type == "waterdrop":
            if (self.x - min <= woodboy.x <= self.x + min and 
                    self.y - min <= woodboy.y <= self.y + min ):
                    woodboy.hitByWaterdrop = True
                    woodboy.die = True
                    self.musicCount += 1
                    if self.musicCount < 2:
                        dieMusic()

        if self.type == "lightning":
            if (self.x - min <=metalgirl.x <= self.x + min 
                    and self.y - min <= metalgirl.y <= self.y + min):
                metalgirl.hitByLightning = True
                metalgirl.die = True
                self.musicCount += 1
                if self.musicCount < 2:
                        dieMusic()

################################################################################

lightning1=  Obstacles(random.randint(200, 400), random.randint(0, 400), "lightning1", "lightning")
lightning2=  Obstacles(random.randint(100, 400), random.randint(0, 400), "lightning2", "lightning")
lightning3 = Obstacles(random.randint(0, 400), random.randint(0, 400), "lightning3", "lightning")
waterdrop1 = Obstacles(random.randint(0, 400), random.randint(0, 400), "waterdrop1", "waterdrop")
waterdrop2 = Obstacles(random.randint(100, 400), random.randint(0, 400), "waterdrop2",  "waterdrop")
waterdrop3 = Obstacles(random.randint(150, 400), random.randint(0, 400), "waterdrop3",  "waterdrop")

################################################################################