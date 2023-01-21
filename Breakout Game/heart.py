import arcade

class Heart(arcade.Sprite):
    def __init__(self,x):
        super().__init__("my-project\session16\icons8-red-heart-48.png")   
        self.center_x=20*x
        self.center_y=480
        self.width=20
        self.height=20