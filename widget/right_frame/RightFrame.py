# import tkinter as tk
# from data.colors import COLORS
#
# from page import Home, MovieList, MovieDetail
#
#
# class RightFrame:
#     """It will hold the pages on the right frame."""
#
#     # class attribute
#     bg_color = COLORS.ORANGE
#
#     # TODO - define the init method
#
#     def add_frame(self):
#         # frame content
#         self.frame_content()
#         self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)
#
#     def frame_content(self, page_name='home'):
#         try:
#             incoming_frame = self.frame
#         except:
#             incoming_frame = self
#         finally:
#             if page_name == 'home':
#                 # add home page
#                 Home(incoming_frame, RightFrame.bg_color)
#             # TODO - create other pages
#
#     # static method -> Class Method (no self parameter)
#     def destroy_children(frame):
#         # destroy the children
#         for child in frame.winfo_children():
#             child.destroy()
#
