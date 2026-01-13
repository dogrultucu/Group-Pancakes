import os
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

import panHome, panFire, panFlip


def __init__(self):
    self.panBrand = "Teflon"
    self.panSize = "250 mm Diameter"
    self.panCoating = "Zircon"
    self.panMaterial = "Aluminum forge"


# 2 robot arms used in conjecture
# Rob1 will be in charge of the pan.
# A consideration of this is that in event of a uncontrolled fire the pan, oil and flame are all under seperate control matters
# Rob 2 will be in charge of 'pancake' elements of the process: mostly squeezing to adhere to a single end-effector


class Rob1:  # Rob1 controls pan: movement and orientation for poses and flipping
    panHome()
    panFire()
    panFlip()


class Rob2:
    {}  #


if __name__ == "__main__":
    panFire
