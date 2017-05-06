from matplotlib import pyplot as plt
import numpy as np
import cv2
from App.MainApp import App
from ImageProcessing.HoughLineProcessing import HoughLineProcessing

app = App()

img = cv2.imread('testCoockie.png')

hough = HoughLineProcessing(app, img)


app.display()
cv2.destroyAllWindows()
