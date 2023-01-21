import random
import arcade

from racket import Racket
from shape import Shape
from heart import Heart
from ball import Ball


class Game(arcade.Window):
    def __init__(self):
        super().__init__(400,500,"BreakGame")
        self.racket=Racket(self)
        self.ball=Ball(self)
        self.shapes=[]
        self.hearts=[]
        self.game_status=" "
        self.game_status1=" "
       

        for i in range(3):
            for j in range(7):
                shape=Shape(30+55*j, 400-20*i)
                self.shapes.append(shape)
        self.background=arcade.load_texture("my-project\session16\cute-abstract-modern-background-free-vector.png")

        for i in range(3):
            self.heart=Heart(i+1)
            self.hearts.append(self.heart)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,400,500, self.background)

        self.racket.draw()
        self.ball.draw()
        for shape in self.shapes:
            shape.draw()

        for heart in self.hearts:
            heart.draw()
        
        arcade.draw_text("score: ",300,480,arcade.color.RED , 17,20)
        arcade.draw_text(self.racket.score , 375,480 ,arcade.color.RED , 15 , 20)

        if self.game_status=="GameOver":
            self.clear()
            arcade.draw_text("GAME OVER",15,250,arcade.color.RED , 45,45)

        if self.game_status1=="win":
            self.clear()
            arcade.draw_text("YOU WIN",40,250,arcade.color.SEA_GREEN , 50,50)

        if len(self.hearts)==0:
            self.game_status="GameOver"

        arcade.finish_render()

    def on_update(self, delta_time: float):
        
        self.racket.move(self)
        self.ball.move(self)
        if arcade.check_for_collision(self.ball,self.racket):
             self.ball.change_y=1

        for shape in self.shapes:
             if arcade.check_for_collision(self.ball,shape):
                self.shapes.remove(shape)
                self.ball.change_y=-1
                self.racket.score +=1

        
        if self.ball.center_y < 0:
            if len (self.hearts)>0:
                self.hearts.pop(-1)
                del self.ball
                self.ball=Ball(self)      


        if len(self.shapes)==0:
            self.game_status1="win"
            
        if self.ball.center_y+15 > self.height:
            self.ball.change_y=-1
        


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.racket.width-30 < x < self.width-self.racket.width+30:
            self.racket.center_x = x


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.RIGHT:
            #self.racket.center_x = self.racket.center_x + self.racket.speed
            self.racket.change_x = 1
        if symbol==arcade.key.LEFT:
            #self.racket.center_x = self.racket.center_x - self.racket.speed
            self.racket.change_x = -1
game=Game()
arcade.run()