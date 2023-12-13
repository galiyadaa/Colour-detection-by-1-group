# Importing necessary libraries
import cv2          # OpenCV for image processing
import numpy as np   # NumPy for numerical operations
import pandas as pd  # Pandas for data manipulation
import argparse     # Argparse for command-line argument parsing

# Creating an argument parser to obtain the image path from the command line
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-i', '--image', required=True, help="Path to the image")
arguments = vars(arg_parser.parse_args())
image_path = arguments['image']

# Reading the image using OpenCV
image = cv2.imread(image_path)

# Declaring global variables for later use
is_clicked = False
red_value = green_value = blue_value = x_position = y_position = 0

# Reading a CSV file with pandas and providing names to each column
# The CSV file is assumed to have columns: "color", "color_name", "hex", "R", "G", "B"
columns = ["color", "color_name", "hex", "R", "G", "B"]
color_data = pd.read_csv('colors.csv', names=columns, header=None)

def get_color_name(rgb, color_data):
    """
    Get the color name that is closest to the provided RGB values.
    Parameters:
    - rgb (tuple): The RGB values as a tuple (R, G, B).
    - color_data (DataFrame): The DataFrame containing color information.

    Returns:
    - str: The name of the closest matching color.
    """
    min_distance = float('inf')  # Initialize with positive infinity
    closest_color_name = "Unknown Color"

    for i in range(len(color_data)):
        color_rgb = color_data.loc[i, ["R", "G", "B"]].values
        d = sum(abs(x - y) for x, y in zip(rgb, color_rgb))

        if d < min_distance:
            min_distance = d
            closest_color_name = color_data.loc[i, "color_name"]

    return closest_color_name

# Example usage:
input_color = (100, 150, 200)
result_color_name = get_color_name(input_color, colors.csv)
print(f"The closest matching color is: {result_color_name}")

def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos, ypos = x, y
        b, g, r = map(int, img[y, x])

