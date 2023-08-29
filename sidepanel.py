
import customtkinter as ctk
from settings import *
from PIL import Image

class SidePanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = SIDE_PANEL_BG)
        self.grid(row = 0, column = 0, sticky = 'news')

        #*WIDGETS
        ViewButtons(self)

class ViewButtons(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(side = 'bottom', fill = 'both', padx = 5, pady = 5)


        #* LAYOUT
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')

        #* WIDGETS
        ctk.CTkButton(self, text  = 'Map', fg_color = BUTTON_COLOR, hover_color = BUTTON_HOVER_COLOR)