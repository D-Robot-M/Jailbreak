import pygame
import os
#http://pixelartmaker.com/art/f632691fc4ff57c	
#http://pixelartmaker.com/art/ab0ad772da82402
class Prisoner():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.images = []
        directory = os.fsencode('images')
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            image = pygame.image.load(os.path.join(os.fsdecode(directory), filename)).convert_alpha()
            self.images.append(pygame.transform.scale(image, (int(image.get_width()/2.5) , int(image.get_height()/2.5))))

        self.currentimage = self.images[0]
        self.rect = self.currentimage.get_rect()
        self.ticker = 0
        self.direction = 'down'

    def draw(self, image):
        image.blit(self.currentimage, [self.x,self.y])
        return image


    def changestate(self):
#    player = pygame.image.load(images[counter])
#    counter = (counter + 1) % len(images) 
        if self.ticker % 20 ==0: 
            if self.dy > 0:
                self.direction = 'down'
                if self.currentimage == self.images[0]:
                    self.currentimage = self.images[1]
                elif self.currentimage == self.images[1]:
                    self.currentimage = self.images[2]                    
                else:
                    self.currentimage = self.images[1]
                 
            elif self.dy < 0:
                self.direction = 'up'
                if self.currentimage == self.images[3]:
                    self.currentimage = self.images[4]
                elif self.currentimage == self.images[4]:
                    self.currentimage = self.images[5]                    
                else:
                    self.currentimage = self.images[4]
            elif self.dx > 0:
                self.direction = 'right'
                if self.currentimage == self.images[8]:
                    self.currentimage = self.images[9]
                else:
                    self.currentimage = self.images[8]

            elif self.dx < 0:
                self.direction = 'left'
                if self.currentimage == self.images[6]:
                    self.currentimage = self.images[7]
                else:
                    self.currentimage = self.images[6]
        self.ticker += 1   

    def move(self):   
        self.move_horz()
        self.move_vert()
        self.changestate()
        self.rect = self.currentimage.get_rect(topleft=(self.x, self.y)) 
    def stop(self):
        self.ticker = 0
        if self.direction == 'down':
            self.currentimage = self.images[0]
        if self.direction == 'up':
            self.currentimage = self.images[3]
        if self.direction == 'right':
            self.currentimage = self.images[8]
        if self.direction == 'left':
            self.currentimage = self.images[6]
        self.dx = 0
        self.dy = 0
    def move_horz(self):
        self.x = self.x + self.dx
    def move_vert(self):
        self.y = self.y + self.dy

    def right(self):
        return self.x + self.currentimage.get_width()
    
    #write a comment
    def left(self):
        return self.x

    #write a comment
    def top(self):
        return self.y
        
    #write a comment
    def bottom(self):
        return self.y + self.currentimage.get_height()   
        
        
        

