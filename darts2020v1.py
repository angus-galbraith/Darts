from tkinter import *
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Combobox


class fiveOhOne:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.configure_gui1()

    def configure_gui1(self):
        self.master.title("501")
        self.master.geometry("600x500")

        # function binding return key to entry box
        self.master.bind('<Return>',lambda e:self.score_Entered())







if __name__=='__main__':
    root = Tk()
    main_app = fiveOhOne(root)
    
    root.mainloop()
    