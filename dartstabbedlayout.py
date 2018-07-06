from tkinter import*
from tkinter import ttk
import os
import pickle


class MainApplication(Frame):

    

    def __init__(self, master):
        self.master = master
        tabControl = ttk.Notebook(self.master)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='501')
        #tabControl.pack(expand=1, fill="both")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Round The Board')
        tabControl.pack(expand=1, fill="both")
         
        
        #self.configure_gui()
        #self.create_widgets()


    #def configure_gui(self):
        
        
        
        


    #def create_widgets(self):

        

        


    

    
if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)
    
    root.mainloop()
