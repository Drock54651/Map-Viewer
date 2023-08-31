
import customtkinter as ctk
from settings import *
from PIL import Image

class SidePanel(ctk.CTkFrame):
    def __init__(self, parent, set_style, update_map):
        super().__init__(parent, fg_color = SIDE_PANEL_BG)
        self.grid(row = 0, column = 0, sticky = 'news')

        #*WIDGETS
        ViewButtons(self, set_style)
        self.history_frame = HistoryFrame(self, update_map)

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
                                         #! lamda needed so function called only when button pressed
                                         #! without lambda, it would essentially just call the func automatically

class HistoryFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, update_map):
        super().__init__(parent)
        self.pack(expand = True, fill = 'both', padx = 5, pady = 5)
        self.font  = ctk.CTkFont(family =TEXT_FONT, size= TEXT_SIZE)
        self.update_map = update_map
        
        

    def add_location_entry(self, location):
        HistoryItem(self, location, self.font, self.update_map)

class HistoryItem(ctk.CTkFrame):
    def __init__(self, parent, location, font, update_map):
        super().__init__(parent)
        self.pack(fill = 'x')

        #* DATA
        self.address = location.address
        town = self.address.split(',')[0]
        country = self.address.split(',')[-1]
        if town == country:
            address_string = town
        
        else:
            address_string = f'{town}, {country}'



        #* WIDGETS
        ctk.CTkButton(self, 
                      text = address_string, 
                      command = lambda: update_map(self.address),
                      font = font, 
                      anchor = 'w', 
                      fg_color = 'transparent', 
                      hover_color = HISTORY_HOVER_COLOR, 
                      text_color = TEXT_COLOR).pack(side = 'left')
        
        ctk.CTkButton(self, 
                      text=  'x', 
                      command = lambda: self.pack_forget(),
                      font = font, 
                      anchor = 'e', 
                      hover_color = HISTORY_HOVER_COLOR, 
                      text_color = TEXT_COLOR,
                      width = 10,
                      fg_color = 'transparent').pack(side = 'left')
