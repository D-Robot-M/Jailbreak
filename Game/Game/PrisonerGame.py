from Player import *
from BasicGame import *
from pygame import *
from pygame.locals import *
from random import *


FPS = 60
class PrisonerGame(BasicGame):
    def __init__(self):
        self.w, self.h = 800, 600
        self.bkg_color = (128,128,128)
        BasicGame.__init__(self, size=(self.w, self.h), fill=(self.bkg_color))
        
        #create walls for the game
        self.LEFT_WALL = 0
        self.RIGHT_WALL = self.w
        self.TOP_WALL = 0
        self.BOTTOM_WALL = self.h
        #create a single person
        self.GameStage = 0
        numpeople = 5
        self.people = []
        for i in range(numpeople):
        	self.people.append(Prisoner(randint(0, self.w), randint(0, self.h)))

        self.player = Player(randint(0, self.w), randint(0, self.h), 0, 0)

    def update(self):
        self.keyPoll()

        self.updateplayer(self.player)
        for ai in self.people:
        	self.updateplayer(ai)
        	ai.randommovement()
    def updateplayer(self, player):
        self.handle_collisions(player)
        player.move()

    def keyDown(self,key):           
        if self.GameStage == 0:
            self.GameStage += 1
            self.player.ticker = 0
        elif self.GameStage == 1:
        	self.GameStage = 0
        	self.player.ticker = 0
    
    def handle_collisions(self, player):
        if player.right() > self.RIGHT_WALL:
        	player.x -= 1
        if player.left() < self.LEFT_WALL:
            player.x += 1  
        if player.top() < self.TOP_WALL:
            player.y += 1
        if player.bottom() > self.BOTTOM_WALL:
            player.y -= 1   


    def keyPoll(self): 
        #use this function if you want to handle multiple key presses
        #this function must be called in update	
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.player.dy = 1
            
        if keys[pygame.K_UP]:
            self.player.dy = -1
        if keys[pygame.K_RIGHT]:
            self.player.dx = 1  
        if keys[pygame.K_LEFT]:
            self.player.dx = -1
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_d] and keys[pygame.K_x]:
            pass #maybe "left" player moves down and right
    def keyUp(self, key):
        self.player.stop()
        
    def mouseUp(self, button, pos):
        if button == 1:
            pass
     
    def mouseDown(self, button, pos):
        if button == 1:
            pass    
        
    def mouseMotion(self, buttons, pos, rel):
        left, mid, right = buttons
        if left == 1:
            pass
             
    def draw(self):
        self.screen.fill(self.bkg_color)
        self.player.draw(self.screen)
        for person in self.people:
        	person.draw(self.screen)
s = PrisonerGame()
s.mainLoop(FPS)