import scene
from game_config import PADDLE_WIDTH, PADDLE_HEIGHT

class Paddle(scene.ShapeNode):
    def __init__(self, position):
        paddle_shape = scene.ui.Path.rect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
        super().__init__(paddle_shape)
        self.fill_color = 'white'
        self.position = position

    def move(self, touch):
        self.position = (touch.location.x, self.position.y)

class PlayerPaddle(Paddle):
    def __init__(self, position):
        super().__init__(position)

class AIPaddle(Paddle):
    def __init__(self, position):
        super().__init__(position)

    def move(self, ball):
        self.position = (ball.position.x, self.position.y)