import tkinter as tk
from PIL import Image, ImageTk

from data.colors import COLORS


class Home:
    """It creates the Home Page."""

    # TODO - define the init method

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        course = tk.Label(self.frame,
                          text='Python Hands-On',
                          font=('Helvetica', 18, 'bold'),
                          fg=COLORS.BLACK,
                          bg=self.bg_color)
        course.place(x=315, y=50)

        instructor = tk.Label(self.frame,
                          text='(Musa Arda)',
                          font=('Helvetica', 18, 'bold'),
                          fg=COLORS.BLACK,
                          bg=self.bg_color)
        # TODO - place instructor at x=344, y=105

        # TODO - render the image

        project = tk.Label(self.frame,
                              text='Capstone Project - Movie Library with Tkinter',
                              font=('Helvetica', 18, 'bold'),
                              fg=COLORS.WHITE,
                              bg=COLORS.BLACK)
        project.place(x=140, y=765)

    def render_image(self):
        load = Image.open('images/home/python_logo.png')
        render = ImageTk.PhotoImage(load)
        img_lb = tk.Label(self.frame, image=render, bg=self.bg_color)
        img_lb.image = render
        img_lb.place(x=136, y=180)
