import cv2
from App.ValueUpdater import ValueUpdater
from Utils import resize, convert_rgb_img

class CannyProcessing:
    """Apply the Canny processing"""
    def __init__(self, app, img):
        self._label = "Canny"
        self._app = app
        self.img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        self.threshold1 = ValueUpdater('Threshold1', 100.0, 0.0, 2000.0, self.apply)
        self.threshold2 = ValueUpdater('Threshold2', 500.0, 0.0, 2000.0, self.apply)

        list_scale = [self.threshold1, self.threshold2]

        app.populate_upper_left_main_frame('Canny', list_scale)
        app.populate_upper_right_main_frame(self._label)
        self.apply()

    def apply(self):
        """Apply the method"""
        self._processed_img = cv2.Canny(self.img_gray, self.threshold1.value, self.threshold2.value)

        self.display()

    def display(self):
        """Display the computed image"""
        img =  resize(self._processed_img)
        self._app.update_img(self._label, img)
