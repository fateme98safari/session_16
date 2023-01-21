import arcade



class Racket(arcade.Sprite):
    def __init__(self,x,y,c):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.change_y=0
        self.color=c
        self.height=70
        self.width=8
        self.speed=4
        self.score=0

    def move(self,game,ball):
        
        if ball.center_x > game.width //2:

            if self.center_y > ball.center_y:
                self.change_y =-1
                
            elif self.center_y < ball.center_y:
                self.change_y =1
                
            self.center_y += self.change_y *self.speed

        if self.center_y < 65:
                self.center_y=65

        if self.center_y > game.height-56:
                self.center_y = game.height-56

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        