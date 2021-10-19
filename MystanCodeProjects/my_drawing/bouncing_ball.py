"""
File: bouncing_ball.py
Name: Jess
-------------------------
This file shows how bouncing ball works,
and the program would be N/A after three times working
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 0
click_or_not = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)

    onmouseclicked(start)


def start(event):
    """
    This program uses the concept of switch to control
    the asynchronous event, and make sure that after three times
    working, the program would turn to be N/A
    """
    global times, click_or_not

    # acceleration (y velocity)
    a = 0

    # the switch controller
    if not times == 3 and not click_or_not:

        while True:

            # this switch make sure that in the process of ball-bouncing
            # mouse click won't interrupt
            click_or_not = True
            ball.move(VX, a)

            # make the bouncing process visible
            pause(DELAY)

            # imitate the freely falling ball
            if ball.x < window.width:
                a += GRAVITY

                # bounce back from the ground
                if ball.y + ball.height >= window.height:
                    a = -a * REDUCE
                    if not a == 0:
                        a += GRAVITY

            # out of window, restart
            else:
                window.add(ball, x=START_X, y=START_Y)
                times += 1
                click_or_not = False
                break


if __name__ == "__main__":
    main()
