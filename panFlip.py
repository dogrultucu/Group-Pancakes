import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


def flipifPancakeBrowning():
    root = os.getcwd()
    # use raw string to avoid confusuion requiring double slash instead (\\)
    imgPath = os.path.join(root, r"machineLearningImageOfPancake\Path.jpeg")
    img = cv.imread(imgPath)

    # Convert BGR to HSV colorspace
    hsvFrame = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Set range for browning colour
    brown_lower = np.array([0, 75, 150], np.uint8)
    brown_upper = np.array([33, 67, 101], np.uint8)

    # Create mask to detect brown color
    brown_mask = cv.inRange(hsvFrame, brown_lower, brown_upper)

    kernel = np.ones((5, 5), "uint8")
    brown_mask = cv.dilate(brown_mask, kernel)
    brown_detected = cv.bitwise_and(img, img, mask=brown_mask)

    # contour to track brown color
    contours, hierarchy = cv.findContours(
        brown_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE
    )

    total_brown_area = 0
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if area > 300:
            total_brown_area += area
            x, y, w, h = cv.boundingRect(contour)
            img = cv.rectangle(img, (x, y), (x + w, y + h), (15, 72, 120), 2)

    # Decide if pancake should flip based on brown area
    if (
        total_brown_area > 5000
    ):  # Adjust threshold as needed (5000 is just random number. Would train ML to detect when edges of pancake brown)
        print(f"Browning detected! Area: {total_brown_area}. Time to flip!")
        return True
        print("Robot 2 arm activated: Spatula removes pancake")
    else:
        print(f"Not brown enough yet. Area: {total_brown_area}")
        return False
