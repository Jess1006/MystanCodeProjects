"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This program through loading many images of the same scene,
delivers an image that ghost out the people and only shows the background.

"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """

    color_dist = ((pixel.red - red)**2 + (pixel.green - green)**2
                  + (pixel.blue - blue)**2)**(1/2)

    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    p_red = 0  # initial value of pixel red
    p_green = 0  # initial value of pixel green
    p_blue = 0  # initial value of pixel blue

    # add up the value of pixel to be averaged at certain (x,y) position
    for pixel in pixels:
        p_red += pixel.red
        p_green += pixel.green
        p_blue += pixel.blue

    # average the value of pixel
    red = p_red // len(pixels)
    green = p_green // len(pixels)
    blue = p_blue // len(pixels)

    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # get the respective RGB averages
    list_of_avg = get_average(pixels)
    avg_red = list_of_avg[0]
    avg_green = list_of_avg[1]
    avg_blue = list_of_avg[2]

    standard = 0  # the box constantly check and renew 'the shortest pixel distance' record through the loop
    count = 0  # to know whether it's the first img that loaded
    best = 0  # initial value

    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)
        count += 1

        # the first loaded img
        if count == 1:
            standard = pixel_dist
            best = pixel

        # others
        else:
            if pixel_dist < standard:
                best = pixel

    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(result.width):
        for y in range(result.height):

            list_of_pixels = []  # list will renew before going to the next position

            # record the pixel at certain (x,y) position for each images
            for img in images:
                pixels = img.get_pixel(x, y)
                list_of_pixels.append(pixels)

            best = get_best_pixel(list_of_pixels)
            b_p = result.get_pixel(x, y)  # b_p goes for blank's pixel
            b_p.red = best.red
            b_p.green = best.green
            b_p.blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
