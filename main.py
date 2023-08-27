import customtkinter as ctk
from settings import *
import tkintermapview

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

        #* WIDGETS
        self.map_widget = MapWidget(self)


        #* RUN
        self.mainloop()

    #* METHODS
    

class MapWidget(tkintermapview.TkinterMapView):
    def __init__(self, parent):
        super().__init__(master  = parent)
        self.grid(row = 0, column = 1, sticky = 'news')

        #TODO: looks at TkinterMapView documentation https://github.com/TomSchimansky/TkinterMapView
        #TODO: use the documentation to update the map style to the terrain view
        self.set_tile_server(TERRAIN_URL)  # google satellite
       
App()