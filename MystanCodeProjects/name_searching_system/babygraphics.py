"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # the width of each timezone
    space = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # upper
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # lower
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        # timezone
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        # year
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # control the line color in sequence
    color_starter = 0

    # the rank position on the line
    space = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / (MAX_RANK - 1)

    for name in lookup_names:
        point_x = []  # record the x coordination
        point_y = []  # record the y coordination
        rank_lst = []  # record the rank

        # collect the information of (each) name, and put into the lists for later drawing
        if name in name_data:
            for i in range(len(YEARS)):
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
                point_x.append(x_coordinate)
                if str(YEARS[i]) in name_data[name]:
                    rank_lst.append(name_data[name][str(YEARS[i])])
                    point_y.append(GRAPH_MARGIN_SIZE + (int(name_data[name][str(YEARS[i])]) - 1) * space)
                else:
                    rank_lst.append('*')
                    point_y.append(GRAPH_MARGIN_SIZE + (MAX_RANK - 1) * space)

        # draw line
        for j in range(len(YEARS)-1):
            canvas.create_line(point_x[j], point_y[j], point_x[j+1], point_y[j+1], width=LINE_WIDTH,
                               fill=COLORS[color_starter])

        # text
        for k in range(len(rank_lst)):
            canvas.create_text(point_x[k]+TEXT_DX, point_y[k], text=(name, rank_lst[k]), anchor=tkinter.SW,
                               fill=COLORS[color_starter])

        # control the line color
        if color_starter == 3:
            color_starter = 0
        else:
            color_starter += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
