import tkinter as tk
from data.colors import COLORS
from PIL import Image, ImageTk


class MovieDetail:
    """Page to hold movie detail."""

    # TODO - define the init method

    def add_frame(self):
        self.add_content()
        self.add_page_title('Movie Detail')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def add_page_title(self, title):
        if self.imdbID != None:
            lbl = tk.Label(self.frame, text=self.movie['Title'], height=3,
                           bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold'))
            lbl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0, 8), sticky='we')
        else:
            lbl = tk.Label(self.frame, text=title, height=3,
                       bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold'))
            lbl.pack(fill=tk.BOTH, padx=(1, 0))


    def add_content(self):
        if self.imdbID != None:
            self.render_image()
            self.get_movie()
            self.render_keys()
            self.render_values()
        else:
            pass

    def render_image(self):
        # TODO - render the large image

    def get_movie(self):
        # TODO - assign the incoming movie to self.movie (you will look in self.movies list)

    def render_keys(self):
        for i, key in enumerate(self.movie.keys()):
            txt = str(key)
            lbl = tk.Label(self.frame, text=txt, height=2, width=12, anchor='w')
            self.fill_bg(lbl, i)
            lbl.grid(row=i+2, column=0, padx=(10, 1))

    def fill_bg(self, widget, i):
        # check if the row (i) is odd
        if i % 2 == 1:
            widget.configure(bg=COLORS.LIST_ODD_LINE)
        else:
            widget.configure(bg=COLORS.LIST_EVEN_LINE)

    def render_values(self):
        # TODO - render the values