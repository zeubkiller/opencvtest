#import numpy as np
import cv2
from App.app import *

def resize(img):
    """Resize an image to half his size"""
    return cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

class CannyProcessing:
    """Apply the Canny processing"""
    def __init__(self, app, img):
        self.img = img.copy()

        self.threshold1 = ValueUpdater('Threshold1', 100.0, 0.0, 2000.0, self.apply)
        self.threshold2 = ValueUpdater('Threshold2', 500.0, 0.0, 2000.0, self.apply)

        list_scale = [self.threshold1, self.threshold2]

        app.create_regions('Canny', list_scale)

        self.apply()

    def apply(self):
        """Apply the method"""
        self.processed_img = cv2.Canny(self.img, self.threshold1.value, self.threshold2.value)
        self.display()

    def display(self):
        """Display the computed image"""
        cv2.imshow('Canny', resize(self.processed_img))
