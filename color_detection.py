# Importing necessary libraries
import cv2          # OpenCV for image processing
import pandas as pd  # Pandas for data manipulation


# Reading the image using OpenCV
image_path = arguments['image']
image = cv2.imread(image_path)

# Declaring global variables for later use
is_clicked = False
red_value = green_value = blue_value = x_position = y_position = 0

# Reading a CSV file with pandas and providing names to each column
# The CSV file is assumed to have columns: "color", "color_name", "hex", "R", "G", "B"
columns = ["color", "color_name", "hex", "R", "G", "B"]
color_data = pd.read_csv('colors.csv', names=columns, header=None)

# function to calculate minimum distance from all colors and get the most matching color
def Get_Color_Name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            color_name = csv.loc[i, "color_name"]
    return color_name

def Draw_Function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, is_clicked
        is_clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('Color detection')
cv2.setMouseCallback('Color detection', Draw_Function)

while (1):

    cv2.imshow("Color detection", img)
    if (is_clicked):

        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = Get_Color_Name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if (r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        is_clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
    
