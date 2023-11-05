import tkinter as tk
from data.colors import COLORS
from data.menus import MENU

# exact import
from widget.button.Button import Button
# from widget.right_frame.RightFrame import RightFrame


class LeftFrame:
    """
    Class for Left Frame to hold the menu items.
    """

    # TODO - define the init method for the LeftFrame
    def __init__(self, window, name):
        self.frame = tk.Frame(
            master = window,
            name = name,
            bg=COLORS.GRAY
        )
        self.master = window
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    # # method for click event of menu buttons -> event handler
    def handle_click(self, event):
        self.manage_button_colors(event)
        page_name = str(event.widget).split('.')[2]
        # print('Page {0} is clicked.'.format(page_name))

        # self is left frame -> master = root
        # right frame is in children of master
        rightFrame = self.master.children['rightFrame']

        # destroy children
        # TODO - call destroy_children() method of RightFrame

        # add new page -> page_name
        # TODO - call frame_content() method of RightFrame

    def add_menus(self):
        # add menus in loop
        for menu_key, menu_text in MENU.items():
            if menu_key == 'about':
                button = Button(self.frame,
                                name = menu_key,
                                text = menu_text,
                                fg = COLORS.ORANGE,
                                bg = COLORS.BLACK,
                                width = 18,
                                height = 2,
                                handle_click = self.handle_click,
                                side = tk.BOTTOM
                                )
            else:
                button = Button(self.frame,
                                name = menu_key,
                                text = menu_text,
                                fg = COLORS.ORANGE,
                                bg = COLORS.BLACK,
                                width = 18,
                                height = 2,
                                handle_click = self.handle_click,
                                side = tk.TOP
                                )

                # if menu_key == 'home':
                #     self.selected_button_color(button.button)

    def manage_button_colors(self, event):
        # clicked button -> event.widget
        # all the menu buttons -> event.widget.master.children
        for child in event.widget.master.winfo_children():
            if child == event.widget:
                child.configure(bg=COLORS.ORANGE, fg=COLORS.WHITE)
            else:
                child.configure(bg=COLORS.BLACK, fg=COLORS.ORANGE)

    # def selected_button_color(self, button):
    #     # tk button configure
    #     # TODO - configure the button as background = ORANGE and foreground = WHITE
