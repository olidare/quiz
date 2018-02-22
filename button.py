import pygame

class Button:
    yellow = (255, 255, 0)

    def text_objects(self,text, font):
        textSurface = font.render(text, True, self.yellow)
        return textSurface, textSurface.get_rect()

    def button(self,Screen, msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos() #gets the coordinates of the mouse
        click = pygame.mouse.get_pressed() # returns a [0] value when clicked

        #if mouse hovers between correct coordinates of button change colour
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(Screen, ac,(x,y,w,h))
            #if mouse is clicked within coordinates, do an action
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(Screen, ic,(x,y,w,h)) #else button just stay in a normal state

        smallText = pygame.font.SysFont("monospace",20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        Screen.blit(textSurf, textRect)



