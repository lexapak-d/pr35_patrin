from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint
from kivy.clock import Clock
from kivy.graphics import Ellipse, Color

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.pos = Vector(self.velocity_x, self.velocity_y) + self.pos

    def update_graphics(self):
        self.ball.pos = self.pos

    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1)
            self.ball = Ellipse(pos=self.pos, size=(50, 50))

class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity_x = randint(4, 8)
        self.ball.velocity_y = 0
        self.ball.velocity = Vector(self.ball.velocity_x, self.ball.velocity_y).rotate(randint(0, 360))
        self.add_widget(self.ball)

    def update(self, dt):
        self.ball.move()
        self.ball.update_graphics()

class PongApp(App):
    def build(self):
        game = PongGame()
        game.ball = PongBall()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()

