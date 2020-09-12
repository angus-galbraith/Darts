from tkinter import *
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Combobox


class fiveOhOne:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.configure_gui1()

    def configure_gui1(self):
        self.master.title("501")
        self.master.geometry("800x600")

        # function binding return key to entry box
        self.master.bind('<Return>',lambda e:self.score_Entered())

        #create frames
        labFrame1 = LabelFrame(self.master, text="Player1 Stats")
        labFrame2 = LabelFrame(self.master, text="Player2 Stats")
        labFrame3 = LabelFrame(self.master, text="Player1 Scores")
        labFrame4 = LabelFrame(self.master, text="Player2  Scores")
        labFrame5 = LabelFrame(self.master, text="Enter Scores")
        
        """
        #make frames visible using grid
        labFrame1.grid(row=0, column=0, rowspan=2, sticky='ew')
        labFrame3.grid(row=0, column=1, sticky='ew')
        labFrame4.grid(row=0, column=2, sticky='ew')
        labFrame2.grid(row=0, column=3, rowspan=2, sticky='ew')
        labFrame5.grid(row=1, column=1, columnspan=2, sticky='ew')
        """
    
        #make frames visible using pack
        labFrame1.pack(side="left",fill="both", expand=True)
        
        labFrame2.pack(side="right", fill="both",  expand=True)
        labFrame5.pack(side="bottom", fill="x",  expand=True)
        labFrame3.pack(side="right", fill="both",  expand=True)
        labFrame4.pack(side="right", fill="both",  expand=True)
        

        #stringvars
        self.pl1name = StringVar()
        self.pl2name = StringVar() 
        self.pl1sets = StringVar()
        self.pl1legs = StringVar()
        self.pl160 = StringVar()
        self.pl180 = StringVar()
        self.pl1100 = StringVar()
        self.pl1140 = StringVar()
        self.pl1180 = StringVar()
        self.pl1avg = StringVar()
        self.pl1chtpc = StringVar()
        self.pl1chtnumbs =StringVar()

        #player to go boolean
        self.player1_togo = True

        
        #frame 1 widgets
        Label(labFrame1, text="Totals").grid(row=0, column=0, sticky='w')
        Label(labFrame1, text="Sets:").grid(row=1, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1sets).grid(row=1, column=1)
        Label(labFrame1, text="Legs:").grid(row=2, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1legs).grid(row=2, column=1)
        Label(labFrame1, text="60+:").grid(row=3, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl160).grid(row=3, column=1)
        Label(labFrame1, text="80+:").grid(row=4, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl180).grid(row=4, column=1)
        Label(labFrame1, text="100+:").grid(row=5, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1100).grid(row=5, column=1)
        Label(labFrame1, text="140+:").grid(row=6, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1140).grid(row=6, column=1)
        Label(labFrame1, text="180:").grid(row=7, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1180).grid(row=7, column=1)
        Label(labFrame1, text="Averages").grid(row=8, column=0, sticky='w')
        Label(labFrame1, text="Score:").grid(row=9, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1avg).grid(row=9, column=1)
        Label(labFrame1, text="Checkout %:").grid(row=10, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1chtpc).grid(row=10, column=1)
        Label(labFrame1, text="Checkout Hit/Thrown:").grid(row=11, column=0, sticky='w')
        Label(labFrame1, textvariable=self.pl1chtnumbs).grid(row=11, column=1)
        

        #stringvars
        self.pl2sets = StringVar()
        self.pl2legs = StringVar()
        self.pl260 = StringVar()
        self.pl280 = StringVar()
        self.pl2100 = StringVar()
        self.pl2140 = StringVar()
        self.pl2180 = StringVar()
        self.pl2avg = StringVar()
        self.pl2chtpc = StringVar()
        self.pl2chtnumbs =StringVar()

        
        #frame 2 widgets
        Label(labFrame2, text="Totals").grid(row=0, column=0, sticky='w')
        Label(labFrame2, text="Sets:").grid(row=1, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2sets).grid(row=1, column=1)
        Label(labFrame2, text="Legs:").grid(row=2, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2legs).grid(row=2, column=1)
        Label(labFrame2, text="60+:").grid(row=3, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl260).grid(row=3, column=1)
        Label(labFrame2, text="80+:").grid(row=4, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl280).grid(row=4, column=1)
        Label(labFrame2, text="100+:").grid(row=5, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2100).grid(row=5, column=1)
        Label(labFrame2, text="140+:").grid(row=6, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2140).grid(row=6, column=1)
        Label(labFrame2, text="180:").grid(row=7, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2180).grid(row=7, column=1)
        Label(labFrame2, text="Averages").grid(row=8, column=0, sticky='w')
        Label(labFrame2, text="Score:").grid(row=9, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2avg).grid(row=9, column=1)
        Label(labFrame2, text="Checkout %:").grid(row=10, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2chtpc).grid(row=10, column=1)
        Label(labFrame2, text="Checkout Hit/Thrown:").grid(row=11, column=0, sticky='w')
        Label(labFrame2, textvariable=self.pl2chtnumbs).grid(row=11, column=1)

        #frame 3 widgets
        self.pl1remaining = StringVar()
        Label(labFrame3, text="Player:").grid(row=0, column=0)
        Label(labFrame3, textvariable=self.pl1name).grid(row=0, column=1)
        Label(labFrame3).grid(row=1)
        Label(labFrame3, text="Remaining").grid(row=2, column=0, columnspan=2, sticky='ew')
        self.remlabel1 = Label(labFrame3, textvariable=self.pl1remaining)
        self.remlabel1.grid(row=3, column=0, columnspan=2)
        self.remlabel1.configure(width=3,background='white', font=(None, 35))
        
        #self.pl1remaining.set(self.pl1dict['score'])
        #self.pl1name.set(game_state.player1)
        


        #frame 4 widgets
        self.pl2remaining = StringVar()
        Label(labFrame4, text="Player:").grid(row=0, column=0)
        Label(labFrame4, textvariable=self.pl2name).grid(row=0, column=1)
        Label(labFrame4).grid(row=1)
        Label(labFrame4, text="Remaining").grid(row=2, column=0, columnspan=2, sticky='ew')
        self.remlabel2 = Label(labFrame4, textvariable=self.pl2remaining)
        self.remlabel2.grid(row=3, column=0, columnspan=2)
        self.remlabel2.configure(width=3,background='white', font=(None, 35))
        #self.pl2remaining.set(self.pl2dict['score'])
        #self.pl2name.set(game_state.player2)

        #frame 5 widgets
        self.playertogo = StringVar()
        self.scoreEntered = StringVar()
        Label(labFrame5, text="    ").grid(row=0, column=0)
        #Label(labFrame5).grid(row=0, column=1)
        #Label(labFrame5).grid(row=0, column=2)
        Label(labFrame5, text="To Go:").grid(row=1, column=1)
        playerLabel = Label(labFrame5, textvariable=self.playertogo)
        playerLabel.grid(row=2, column=1)
        playerLabel.configure( font=(None, 20))
        
        self.number_entry = Entry(labFrame5, textvariable=self.scoreEntered, width=5)
        self.number_entry.grid(row=2, column=2)
        self.number_entry.configure(background='white', font=(None, 20))
        self.number_entry.focus()









if __name__=='__main__':
    root = Tk()
    main_app = fiveOhOne(root)
    
    root.mainloop()
    