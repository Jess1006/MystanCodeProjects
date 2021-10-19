"""
File: draw_line.py
Name: Jess
-------------------------
This file let user draws line(s) depends on those two points
user clicked.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant control the size of the hollow circle
SIZE = 10

# Global variables
window = GWindow()
click_number = 0
ho_c = GOval(SIZE, SIZE)
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(click)


def click(event):
    """
    This program uses the concept of switch to control
    the box that take over(save) the position information of the click,
    then use those information to draw the line
    """
    global click_number, ho_c, x1, y1

    if click_number == 0:
        x1 = event.x
        y1 = event.y
        ho_c.filled = False
        window.add(ho_c, x=x1 - SIZE / 2, y=y1 - SIZE / 2)
        # switch
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y
        line = GLine(x1, y1, x2, y2)
        window.remove(ho_c)
        window.add(line)
        # switch
        click_number = 0


if __name__ == "__main__":
    main()
