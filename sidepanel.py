
import customtkinter as ctk
from settings import *
from PIL import Image

class SidePanel(ctk.CTkFrame):
    def __init__(self, parent, set_style):
        super().__init__(parent, fg_color = SIDE_PANEL_BG)
        self.grid(row = 0, column = 0, sticky = 'news')

        #*WIDGETS
        ViewButtons(self, set_style)

class ViewButtons(ctk.CTkFrame):
    def __init__(self,parent, set_style):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(side = 'bottom', fill = 'both', padx = 5, pady = 5)


        #* LAYOUT
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        
        #* IMAGES
        map_image = ctk.CTkImage(dark_image = Image.open(map_image_path), light_image = Image.open(map_image_path))
        terrain_image = ctk.CTkImage(dark_image = Image.open(terrain_image_path), light_image = Image.open(terrain_image_path))
        paint_image = ctk.CTkImage(dark_image = Image.open(paint_image_path), light_image = Image.open(paint_image_path))
        #* WIDGETS
        ctk.CTkButton(self, command = lambda: set_style('map'), width = 60, text  = '', image = map_image, fg_color = BUTTON_COLOR, hover_color = BUTTON_HOVER_COLOR).grid(row = 0, column = 0, sticky = 'w')
        ctk.CTkButton(self, command = lambda: set_style('terrain'), width = 60, text  = '', image = terrain_image, fg_color = BUTTON_COLOR, hover_color = BUTTON_HOVER_COLOR).grid(row = 0, column = 1)
        ctk.CTkButton(self, command = lambda: set_style('paint'), width = 60, text  = '', image = paint_image, fg_color = BUTTON_COLOR, hover_color = BUTTON_HOVER_COLOR).grid(row = 0, column = 2, sticky = 'e')