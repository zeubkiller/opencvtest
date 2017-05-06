from Tkinter import Frame, Button, Scale, Tk, Label, X, LEFT

class ValueUpdater:
    """Create a parameter that can be displayed as a scale button"""
    def __init__(self, label, value, top, bottom, callback):
        self._value = value
        self._label = label
        self._top = top
        self._bottom = bottom
        self._callback = callback

    def create_scale(self, region):
        """ Create scale for this parameter"""
        if isinstance(self._value, int):
            resolution = 1
        else:
            resolution = 0.001
        frame = Frame(region)
        label = Label(frame, text=self._label)
        label.pack()
        scale = Scale(frame, from_=self._top, to=self._bottom, command=self.update_value, resolution=resolution)
        scale.set(self._value)
        scale.pack()
        frame.pack(side=LEFT)

    @property
    def value(self):
        """Return the value of the parameter"""
        return self._value

    def convert_value(self, value):
        """Convert a value in int or float depending on the internal value"""
        if isinstance(value, int):
            new_value = int(value)
        else:
            new_value = float(value)
        return new_value

    def update_value(self, value):
        """Update the internal value and call the callback"""
        self._value = self.convert_value(value)
        self._callback()
