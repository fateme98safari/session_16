import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,a,b):
        super().__init__("my-project\session16\icons8-beach-ball-48.png")
        self.center_x=a//2
        self.center_y=b//2
        self.change_x=random.choice([-1,1])
        self.change_y=random.choice([-1,1])
        self.redius=17
        self.height=34
        self.width=34
        self.speed=5


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed