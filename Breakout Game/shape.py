import arcade

class Shape(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("my-project\session16\icons8-red-heart-48.png")
        self.center_x=x
        self.center_y=y
        self.width=60
        self.height=60