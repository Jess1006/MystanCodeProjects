"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Width of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 100  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 4  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # construction
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'steelblue'
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'steelblue'
        self.window.add(self.ball, x=(window_width - 2 * ball_radius) / 2, y=(window_height - 2 * ball_radius) / 2)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0
        self._set_ball_velocity()

        # velocity getter
        self.get_ball_x_velocity()
        self.get_ball_y_velocity()

        # Initialize our mouse listeners
        self.is_game_start = False
        onmouseclicked(self._start)
        onmousemoved(self._paddle_swift)

        # Draw bricks
        self._num_bricks = 0
        position_x = 0
        position_y = brick_offset
        color = 'navy'
        for i in range(brick_rows // (brick_rows // 5)):
            for j in range(brick_rows // 5):
                for k in range(brick_cols):
                    self.brick = GRect(brick_width, brick_height)
                    self.brick.filled = True
                    self.brick.fill_color = color
                    self.window.add(self.brick, x=position_x, y=position_y)
                    self._num_bricks += 1
                    position_x += (brick_width + brick_spacing)
                position_x = 0
                position_y += (brick_height + brick_spacing)
            if i == 0:
                color = 'steelblue'
            elif i == 1:
                color = 'wheat'
            elif i == 2:
                color = 'beige'
            elif i == 3:
                color = 'floralwhite'
            elif i == 4:
                color = 'ivory'
            elif i == 5:
                color = 'gold'
            elif i == 6:
                color = 'orange'

        # initial probe ready to re-assign
        self._probe1 = 0
        self._probe2 = 0
        self._probe3 = 0
        self._probe4 = 0

        # whether collision has happened
        self.collide = False

        # lose label
        self.lose = GLabel('Game Over :(', x=self.window.width/6, y=self.window.height/2)
        self.lose.font = 'Times-40-bold'

        # win label
        self.win = GLabel(' You win!! :)', x=self.window.width/6, y=self.window.height/2)
        self.win.font = 'Times-40-bold'

    # below are all methods
    def _start(self, event):
        """
        the switch control the game to start and set the initial velocity
        :param event: mouse click
        :return: True
        """
        self.is_game_start = True
        self._set_ball_velocity()

    # setter
    def _set_ball_velocity(self):
        """
        assign the velocity x in random, and assign the velocity y
        with constant, initial y speed
        """
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED

    # getter
    def get_ball_x_velocity(self):
        return self._dx

    def get_ball_y_velocity(self):
        return self._dy

    def _paddle_swift(self, mouse):
        """
        when mouse move, paddle move.
        all the movements would be limit inside the game window,
        with y position remains unchanged

        :param mouse: track mouse move
        :return: moving-paddle aligns with the mouse position
        """
        if 0 <= mouse.x - self.paddle.width / 2 <= self.window.width - self.paddle.width:
            self.paddle.x = mouse.x - self.paddle.width / 2

        if mouse.y + self.paddle.height / 2 == self.paddle.y:
            self.paddle.y = mouse.y - self.paddle.height / 2

    def collision_or_not(self):
        """
        Using each probe to detect whether there is the collision or not
        If yes, reassign the collision to 'True'.
        And with methods 'what is that_' to go through what involve in this collision,
        determines the next move
        """
        self._probe1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self._probe2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self._probe3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        self._probe4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if self._probe1 is None:
            if self._probe2 is None:
                if self._probe3 is None:
                    if self._probe4 is None:
                        self.collide = False

                    else:
                        self.collide = True
                        self._what_is_this_4()
                else:
                    self.collide = True
                    self._what_is_this_3()
            else:
                self.collide = True
                self._what_is_this_2()
        else:
            self.collide = True
            self._what_is_this_1()

    # work for probe 1
    def _what_is_this_1(self):
        if self._probe1 == self.paddle:
            pass
        else:
            self.window.remove(self._probe1)
            self._num_bricks -= 1

    # work for probe 2
    def _what_is_this_2(self):
        if self._probe2 == self.paddle:
            pass
        else:
            self.window.remove(self._probe2)
            self._num_bricks -= 1

    # work for probe 3
    def _what_is_this_3(self):
        if self._probe3 == self.paddle:
            pass
        else:
            self.window.remove(self._probe3)
            self._num_bricks -= 1

    # work for probe 4
    def _what_is_this_4(self):
        if self._probe4 == self.paddle:
            pass
        else:
            self.window.remove(self._probe4)
            self._num_bricks -= 1

    def restart(self):
        """
        when the ball falls out of the window,
        and the attempts are still in the range,
        then restart the game with lives minus 1
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # the switch turn to off for next click to start
        self.is_game_start = False

    def ball_is_out_of_window(self):
        """
        detect ball is falling out of window or not
        :return: boolean
        """
        if self.ball.y > self.window.height:
            return True
        else:
            return False

    def bricks_cleared(self):
        """
        to know whether all the bricks have been removed
        :return: boolean
        """
        if self._num_bricks == 0:
            return True
        else:
            return False


