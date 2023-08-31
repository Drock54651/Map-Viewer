import customtkinter as ctk
from settings import *
import tkintermapview
from geopy.geocoders import Nominatim #!
from sidePanel import SidePanel
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        self.geometry('1200x800 + 100 + 50')
        self.minsize(800,600)
        self.title('Map')
        self.iconbitmap('map.ico')


        #* LAYOUT
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 2 , uniform = 'a')
        self.columnconfigure(1, weight = 8 , uniform = 'a')

        
        #* DATA
        self.input_string = ctk.StringVar()



        #* WIDGETS
        self.map_widget = MapWidget(self, self.input_string, self.submit_location)
        self.side_panel = SidePanel(self, self.map_widget.set_style, self.map_widget.set_address)


        #* RUN
        self.mainloop()


    #* METHODS

    def submit_location(self, event):

        #* GET DATA
        geolocator = Nominatim(user_agent = 'my-user') 
        location = geolocator.geocode(self.input_string.get(), language = 'en') 
                                                                              
       
        #* UPDATE MAP
        if location:
            self.map_widget.set_address(location.address) 
            
            self.side_panel.history_frame.add_location_entry(location)

            #* CLEAR INPUT
            self.input_string.set('')

       
        else:
           
            self.map_widget.location_entry.error_animation()

class MapWidget(tkintermapview.TkinterMapView):
    def __init__(self, parent, input_string, submit_location):
        super().__init__(master  = parent)
        self.grid(row = 0, column = 1, sticky = 'news')

        
        #* ENTRY FOR LOCATION
        self.location_entry = LocationEntry(self, input_string, submit_location)
    
    def set_style(self, view_style):
        
        #* STYLE CHANGE
        
        if view_style == 'map':
            self.set_tile_server(MAIN_URL)
            
        if view_style == 'terrain':
            self.set_tile_server(TERRAIN_URL)  # google satellite
        

        if view_style == 'paint':
            self.set_tile_server(PAINT_URL)

            
class LocationEntry(ctk.CTkEntry):
    def __init__(self, parent, input_string, submit_location):
        self.color_index = 15 #! for the color range in settings

        color = COLOR_RANGE[self.color_index]
        self.error = False
        super().__init__(parent, 
                         textvariable = input_string,
                         corner_radius = 0,
                         border_width = 4,
                         fg_color =  ENTRY_BG,
                         border_color = f'#F{color}{color}',
                         text_color = TEXT_COLOR,
                         font = ctk.CTkFont(family = TEXT_FONT, size  = TEXT_SIZE))
        
        self.place(relx = .5, rely = .95, anchor = 'center')

        self.bind('<Return>', submit_location)

        input_string.trace('w', self.remove_error)
    
    def error_animation(self):
        
        self.error = True
        if self.color_index > 0:
            self.color_index -= 1
            
            
            border_color = f'#F{COLOR_RANGE[self.color_index]}{COLOR_RANGE[self.color_index]}' 

            
            text_color = f'#{COLOR_RANGE[-self.color_index - 1]}00' 

            self.configure(border_color = border_color, text_color = text_color)

        
            self.after(40,self.error_animation)
    
    def remove_error(self, *args):
        if self.error:

            self.configure(border_color = ENTRY_BG, text_color = TEXT_COLOR, )
            self.color_index = 15


App()