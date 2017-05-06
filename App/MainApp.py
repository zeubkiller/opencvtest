from Tkinter import *
from ttk import *
from PIL import Image, ImageTk

class App:
    """Main window of our app"""
    def __init__(self):
        self.main_window = Tk()

        self._dict_frame_img = {}

        """
        Main frame
        |   Up   |
        **********
        | Bottom |
        """
        
        self.upper_main_frame = Frame(self.main_window)
        self.upper_main_frame.grid(row=0, column=0)

        self.bottom_main_frame = Frame(self.main_window)
        self.bottom_main_frame.grid(row=1, column=0)

        
        """
        Upper frame
        | Left  | Right  |
        ******************
        |     Bottom     |
        """
        self.upper_left_main_frame = Frame(self.upper_main_frame)
        self.upper_left_main_frame.grid(row=0, column=0)
        
        self.upper_right_main_frame = Frame(self.upper_main_frame)
        self.upper_right_main_frame.grid(row=0, column=1)

        self.upper_right_tabbed_view = Notebook(self.upper_right_main_frame)

        #Close button
        close_button = Button(self.bottom_main_frame, text='Close', command=self.quit)
        close_button.pack(fill=X)

    def quit(self):
        """Quit the application"""
        self.main_window.quit()
    def display(self):
        """Display the application"""
        self.main_window.mainloop()

    def populate_upper_left_main_frame(self, label, list_scale):
        """Create region from a list of parameter"""
        region = Frame(self.upper_left_main_frame)
        label = Label(region, text=label)
        label.pack(fill=X)
        region.pack()

        for scale in list_scale:
            scale.create_scale(region)

    def populate_upper_right_main_frame(self, label):
        frame = Frame(self.upper_right_tabbed_view)

        self.upper_right_tabbed_view.add(frame, text=label)
        self.upper_right_tabbed_view.pack(side=RIGHT)

        self._dict_frame_img[label] = frame

    def update_img(self, label, img):
        frame = self._dict_frame_img[label]
        for widget in frame.winfo_children():
            widget.destroy()

        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(im)

        label = Label(frame, image=imgtk)
        label.image = imgtk
        label.pack()

