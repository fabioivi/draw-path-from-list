##################################
# Imports
##################################
import matplotlib.pyplot as plt

##################################
# Constants
##################################
SHIFT = 10
ADJUST_SIZE_NUMBER = 18
SIZE_DEFAULT = 17

##################################
# Functions
##################################
def draw_label(x,y,label):
    label = label + 1
    if label >= 10:
        plt.text(x - ADJUST_SIZE_NUMBER, y - SHIFT, label, fontsize=10, weight="bold")
    else:
        plt.text(x - SHIFT , y - SHIFT, label, fontsize=10, weight="bold")

def draw_line_label (x,y,label):
    plt.plot(x, y, marker = 'o', markersize=SIZE_DEFAULT)
    draw_label(x[0], y[0], label)

def get_point (item):
    x , y = item
    return x , y

def draw_path(list_points):
    index = 0
    for index in range(len(list_points) - 1):
        x1 , y1 = get_point(list_points[index])
        x2 , y2 = get_point(list_points[index + 1])
        x = [x1, x2]
        y = [y1, y2]
        draw_line_label(x, y, index)
    last_index = index + 1
    last_x , last_y = get_point(list_points[last_index])
    draw_label(last_x,last_y,last_index)
    plt.show()

##################################
# Main - Tests
##################################
ex =    [
            [565.0, 575.0], [345.0, 750.0], [945.0, 685.0], 
            [880.0, 660.0], [845.0, 655.0], [25.0, 185.0], 
            [0, 600], [200, 600], [350, 500], [600, 650], 
            [800, 500], [900, 300], [600, 200], [200, 400],
            [50, 700]
        ]

draw_path(ex)


