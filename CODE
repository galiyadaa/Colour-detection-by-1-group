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
