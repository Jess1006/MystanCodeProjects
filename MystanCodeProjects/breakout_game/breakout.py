"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program makes the simple game "Breakout"
with the class breakoutgraphics made our own, and methods as well.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES


    # getter: get the initial ball velocity
    dx = graphics.get_ball_x_velocity()
    dy = graphics.get_ball_y_velocity()

    # animation while loop here
    while True:
        # pause
        pause(FRAME_RATE)

        # check 1
        if graphics.ball_is_out_of_window():
            lives -= 1
            if lives > 0:
                graphics.restart()

            else:
                graphics.window.add(graphics.lose)
                break

        # check 2
        if graphics.bricks_cleared():
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.win)
            break

        # check 3 & update
        if graphics.is_game_start:
            graphics.ball.move(dx, dy)
            graphics.collision_or_not()
            if graphics.collide:
                dy *= -1

            else:
                if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx

                if graphics.ball.y < 0:
                    dy = -dy


if __name__ == '__main__':
    main()
