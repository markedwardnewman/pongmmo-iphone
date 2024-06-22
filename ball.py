import scene
from game_config import BALL_RADIUS

class Ball(scene.ShapeNode):
    def __init__(self, play_area_rect):
        ball_shape = scene.ui.Path.oval(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)
        super().__init__(ball_shape)
        self.fill_color = 'white'
        self.position = play_area_rect.center()
        self.dx = 5  # Horizontal speed
        self.dy = 5  # Vertical speed

    def move(self):
        self.position += (self.dx, self.dy)

    def check_bounds(self, play_area_rect, player_paddle, ai_paddle):
        # Check collision with top and bottom
        if self.position.y + BALL_RADIUS >= play_area_rect.y + play_area_rect.h or self.position.y - BALL_RADIUS <= play_area_rect.y:
            self.dy = -self.dy

        # Check collision with paddles
        if player_paddle.frame.contains_point(self.position - (0, BALL_RADIUS)):
            self.dy = -self.dy
        elif ai_paddle.frame.contains_point(self.position + (0, BALL_RADIUS)):
            self.dy = -self.dy

        # Check if the ball is out of bounds horizontally and bounce
        if self.position.x - BALL_RADIUS <= play_area_rect.x or self.position.x + BALL_RADIUS >= play_area_rect.x + play_area_rect.w:
            self.dx = -self.dx  # Bounce back horizontally

        # Check if the ball is out of bounds vertically and reset
        if self.position.y - BALL_RADIUS <= play_area_rect.y or self.position.y + BALL_RADIUS >= play_area_rect.y + play_area_rect.h:
            self.position = play_area_rect.center()
            self.dy = -self.dy  # Change direction on reset to avoid getting stuck

