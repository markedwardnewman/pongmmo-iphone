import scene
from ball import Ball
from paddle import PlayerPaddle, AIPaddle
from game_config import PADDLE_HEIGHT

class PongGame(scene.Scene):
    def setup(self):
        self.screen = self.bounds
        self.background_color = (0.1, 0.1, 0.3)  # Dark blue background

        PLAY_AREA_WIDTH = self.screen.w
        PLAY_AREA_HEIGHT = self.screen.h - 200  # Adjust height as needed for the play area

        self.play_area_rect = scene.Rect(
            (self.screen.w - PLAY_AREA_WIDTH) / 2,
            (self.screen.h - PLAY_AREA_HEIGHT) / 2,
            PLAY_AREA_WIDTH,
            PLAY_AREA_HEIGHT
        )

        self.play_area_color = scene.ShapeNode(scene.ui.Path.rect(0, 0, PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT))
        self.play_area_color.fill_color = (0.5, 0.5, 1)  # Light blue for the play area
        self.play_area_color.position = self.play_area_rect.center()
        self.add_child(self.play_area_color)

        self.ball = Ball(self.play_area_rect)
        self.player_paddle = PlayerPaddle(scene.Point(self.play_area_rect.center().x, self.play_area_rect.y + PADDLE_HEIGHT))
        self.ai_paddle = AIPaddle(scene.Point(self.play_area_rect.center().x, self.play_area_rect.y + PLAY_AREA_HEIGHT - PADDLE_HEIGHT))

        self.add_child(self.ball)
        self.add_child(self.player_paddle)
        self.add_child(self.ai_paddle)

    def update(self):
        self.ball.move()
        self.ball.check_bounds(self.play_area_rect, self.player_paddle, self.ai_paddle)
        self.ai_paddle.move(self.ball)

    def touch_moved(self, touch):
        self.player_paddle.move(touch)

if __name__ == '__main__':
    scene.run(PongGame(), show_fps=True)


