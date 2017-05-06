from matplotlib import pyplot as plt
import numpy as np
import cv2
from App.MainApp import App
from ImageProcessing.HoughLineProcessing import HoughLineProcessing

def openCv():
    img = cv2.imread('testCoockie.png')

    hough = HoughLineProcessing(app, img)

app = App()

openCv()

app.display()
cv2.destroyAllWindows()
