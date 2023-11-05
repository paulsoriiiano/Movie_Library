"""
This is the main file of Movie Library:
Pages:
    1- Home
    2- Movie List
    3- Movie Detail

https://www.imdb.com/chart/top/
"""
import tkinter as tk
from widget import Window
from widget import LeftFrame

if __name__ == '__main__':
    pass
    # Root Window
    root = Window("Movie Library")

    # LEFT FRAME
    left_frame = LeftFrame(root.window, 'leftFrame')

    # RIGHT FRAME
    # TODO - Create the right frame by calling RightFrame class

    # start root window -> mainloop()
    # TODO - start the main window (root)
    root.start_method()
