import arcade

class Racket(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x=game.width//2
        self.center_y=20
        self.change_x=0
        self.width=80
        self.height=8
        self.color=arcade.color.RED_DEVIL
        self.speed=4
        self.score=0
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,self.width,self.height,self.color)
        

    def move(self,game):
        self.center_x += self.change_x * self.speed

        if self.center_x + (self.width//2) == game.width:
            self.change_x = -1
        if self.center_x - (self.width//2) ==0:
            self.change_x = 1 