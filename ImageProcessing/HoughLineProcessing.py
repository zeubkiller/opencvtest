import cv2
import numpy as np
from App.ValueUpdater import ValueUpdater
from Utils import resize, convert_rgb_img
from CannyProcessing import CannyProcessing

class HoughLineProcessing:
    """Apply the Hough line processing"""
    def __init__(self, app, img):
        self._label = "Hough"
        self._original_img = img.copy()
        self._canny = CannyProcessing(app, img)
        self._app = app

        self._rho = ValueUpdater('Rho', 1, 0.1, 10, self.apply, is_int=False)
        self._theta = ValueUpdater('Theta', np.pi/180, 0.0, 2 * np.pi, self.apply, is_int=False)
        self._threshold = ValueUpdater('Threshold', 100, 0, 2000, self.apply)
        self._min_line_length = ValueUpdater('MinLineLength', 1, 0, 2000, self.apply)
        self._max_line_gap = ValueUpdater('MaxLineGap', 100, 0, 2000, self.apply)


        list_scale = [self._rho, self._theta, self._threshold
        , self._min_line_length, self._max_line_gap]

        app.populate_upper_left_main_frame(self._label, list_scale)

        app.populate_upper_right_main_frame(self._label)

        self.apply()

    def apply(self):
        """Apply the method"""
        lines = cv2.HoughLinesP(self._canny._processed_img, self._rho.value, self._theta.value, int(self._threshold.value), minLineLength=int(self._min_line_length.value), maxLineGap=int(self._max_line_gap.value))
        
        self._processed_img = self._original_img.copy()

        if lines != None:
            for index in range(0, len(lines)):
                for x1, y1, x2, y2 in lines[index]:
                    cv2.line(self._processed_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        self.display()

    def display(self):
        """Display the computed image"""
        self._canny.display()
        img = resize(convert_rgb_img(self._processed_img))
        self._app.update_img(self._label, img)
