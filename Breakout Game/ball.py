import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__("my-project\session16\icons8-ball-64.png")
        self.center_x=game.width//2
        self.center_y=40
        self.change_x=random.choice([-1,1])
        self.change_y=1
        self.width=30
        self.height=30
        self.redius=15
        self.speed=4

    def move(self,game):
        self.center_x +=self.change_x *self.speed
        self.center_y +=self.change_y *self.speed

        if self.center_x + self.redius > game.width:
            self.change_x= -1
        
        if self.center_x - self.redius < 0:
            self.change_x= 1