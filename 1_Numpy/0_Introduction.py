import numpy as np
#
# pi = 3.1415
#
#
# def area_of_circle(r):
#     area = pi * r * r
#     return area
#
# print("Area of circle:   ", area_of_circle(4))


def area_of_circle_2(r):
    area2 = np.pi * np.power(r, 2)
    return area2


print("Area of circle 2: ", area_of_circle_2(4))


