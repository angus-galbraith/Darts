from tkinter import*
from tkinter.ttk import Frame, Style, Label, Combobox
import os
import pickle
import fiveohone
import roundtheboard
import dartsdb
import viewstats



class MainApplication(Frame):

    

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        #Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()
        


    def configure_gui(self):
        self.master.title("Darts")
        self.master.geometry("470x200")


    def create_widgets(self):

        #variables
        

        #padding
        Label(self.master).grid(row=0, column=0)
        Label(self.master).grid(row=0, column=1)
        Label(self.master).grid(row=2, column=0)
        Label(self.master).grid(row=4, column=0)
        

        #buttons
        Button(self.master, text="501", command=self.five_oh_one).grid(row=1, column=2)
        Button(self.master, text="Round the Board", command=self.round_the_board).grid(row=1, column=3)
        Button(self.master, text="Finishes", command=self.finishes).grid(row=1, column=4)
        Button(self.master, text="Cricket", command=self.cricket).grid(row=1, column=5)
        Button(self.master, text="View Stats", command=self.view_stats).grid(row=1, column=6)




    def five_oh_one(self):

        #stringvarsself.rtb_entry = StringVar()
        self.ply1entry = StringVar()
        self.ply2entry = StringVar()
        self.setsentry = StringVar()
        self.legsentry = StringVar()

        #widgets
        self.ply1Label = Label(self.master, text="Player 1:")
        self.ply1Label.grid(row=3, column=3)
        self.ply1Entry = Entry(self.master, textvariable=self.ply1entry, width=10)
        self.ply1Entry.grid(row=3, column=4, sticky='e')
        self.ply2Label = Label(self.master, text="Player 2:")
        self.ply2Label.grid(row=4, column=3)
        self.ply2Entry = Entry(self.master, textvariable=self.ply2entry, width=10)
        self.ply2Entry.grid(row=4, column=4, sticky='e')
        self.setsLabel = Label(self.master, text="Number of Sets:")
        self.setsLabel.grid(row=5, column=3)
        self.setsBox = Combobox(self.master, textvariable=self.setsentry, width=5)
        self.setsBox['values'] = ( 1, 3, 5, 7, 9)
        self.setsBox.current(1)
        self.setsBox.grid(row=5, column=4)
        self.legsLabel = Label(self.master, text="Number of Legs:")
        self.legsLabel.grid(row=6, column=3)
        self.legsBox = Combobox(self.master, textvariable=self.legsentry, width=5)
        self.legsBox['values'] = ( 1, 3, 5, 7, 9)
        self.legsBox.current(2)
        self.legsBox.grid(row=6, column=4)
        self.plyButton = Button(self.master, text="Start Game", command=self.fiveohone_start)
        self.plyButton.grid(row=7, column=4)
        

    def fiveohone_start(self):
        player1name = self.ply1entry.get()
        player2name = self.ply2entry.get()
        numbersets = int(self.setsentry.get())
        numberlegs = int(self.legsentry.get())
        self.newWindow = Toplevel(self.master)
        self.app = fiveohone.fiveOhOne(self.newWindow, player1name, player2name, numbersets, numberlegs)
        
        


    def round_the_board(self):
        self.rtbLabel = Label(self.master, text="Player Name")
        self.rtbLabel.grid(row=3, column=3)
        self.rtbEntry = Entry(self.master, textvariable=self.rtb_entry, width=10)
        self.rtbEntry.grid(row=3, column=4, sticky='e')
        self.rtbEntry.focus()
        self.rtbButton = Button(self.master, text="Start Game", command=self.rtb_start)
        self.rtbButton.grid(row=5, column=3, columnspan=2)
        

    def rtb_start(self):
        playername = self.rtb_entry.get()
        print(playername)
        self.rtbLabel.destroy()
        self.rtbEntry.destroy()
        self.rtbButton.destroy()
        self.newWindow = Toplevel(self.master)
        self.app = roundtheboard.roundTheBoard(self.newWindow, playername)
            
        
        



    def finishes(self):
        pass


    def cricket(self):
        pass


    def view_stats(self):
        self.newWindow = Toplevel(self.master)
        self.app = viewstats.viewStats(self.newWindow)



    

        
        
        
if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)
    
    root.mainloop()
    conn = dartsdb.connect()
