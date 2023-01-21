import random
import arcade


from ballclass import Ball
from racketclass import Racket





class Game(arcade.Window):
    def __init__(self):
        super().__init__(700,400,"PongGame")
        arcade.set_background_color(arcade.color.DARK_SEA_GREEN)
        self.racket1=Racket(24,self.height//2,arcade.color.PURPLE_HEART)
        self.racket2=Racket(self.width-24 , self.height//2 , arcade.color.DARK_PINK)
        self.ball=Ball(self.width,self.height)
        self.game_status1=" "
        self.game_status2=" "

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2 , self.height//2,680,380,arcade.color.WHITE,7)
        arcade.draw_line(self.width//2, 20 , self.width//2 ,380,arcade.color.WHITE,7 )
        self.racket1.draw()
        self.racket2.draw()
        self.ball.draw()
        if self.game_status1=="Goal":
           arcade.draw_text(self.racket2.score,(self.width//2)-30,self.height-70,arcade.color.RED,30,20)
        if self.game_status2=="Goal":
           arcade.draw_text(self.racket1.score,(self.width//2)+10,self.height-70,arcade.color.RED,30,20)



        arcade.finish_render()


    def on_update(self, delta_time: float):
    
        self.ball.move()
        self.racket2.move(self,self.ball)

        if self.ball.center_y <30 or  self.ball.center_y>self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.racket1 , self.ball) or arcade.check_for_collision(self.racket2 , self.ball):
            self.ball.change_x *=-1
        
        if self.ball.center_x < 0:
           self.racket1.score +=1
           self.game_status2="Goal"
           del self.ball
           self.ball=Ball(self.width,self.height)

        if self.ball.center_x > self.width +10:
            self.racket2.score +=1
            self.game_status1="Goal"
            del self.ball
            self.ball=Ball(self.width,self.height)


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.racket1.height < y < self.height-self.racket1.height:
            self.racket1.center_y = y




game=Game()
arcade.run()