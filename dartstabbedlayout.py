from tkinter import*
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Combobox, Notebook
import os
import pickle


class MainApplication(Frame):

    

    def __init__(self, master):
        self.master = master
        tabControl = Notebook(self.master)
        self.tab1 = Frame(tabControl)
        tabControl.add(self.tab1, text='501')
        #tabControl.pack(expand=1, fill="both")
        tab2 = Frame(tabControl)
        tabControl.add(tab2, text='Round The Board')
        tabControl.pack(expand=1, fill="both")
         
        
        self.configure_gui()
        self.create_widgets()
        self.start_window()


    def configure_gui(self):

        self.master.title("501")
        self.master.geometry("600x500")

        # function binding return key to entry box
        self.master.bind('<Return>',lambda e:self.score_Entered())

        #create frames
        self.labFrame1 = LabelFrame(self.tab1, text="Player1 Stats")
        self.labFrame2 = LabelFrame(self.tab1, text="Player2 Stats")
        self.labFrame3 = LabelFrame(self.tab1, text="Player1 Scores")
        self.labFrame4 = LabelFrame(self.tab1, text="Player2  Scores")
        self.labFrame5 = LabelFrame(self.tab1, text="Enter Scores")
        #self.labFrame6 = LabelFrame(self.master, text="Additional info")

        #make frames vis(ible
        self.labFrame1.grid(row=0, column=0, rowspan=2, sticky='ns')
        self.labFrame3.grid(row=0, column=1)
        self.labFrame4.grid(row=0, column=2)
        self.labFrame2.grid(row=0, column=3, rowspan=2, sticky='ns')
        self.labFrame5.grid(row=1, column=1, columnspan=2, sticky='ew')
        #self.labFrame6.grid(row=3, column=1, columnspan=2, sticky='ew')
        
        
        
        


    def create_widgets(self):

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
        Label(self.labFrame1, text="Totals").grid(row=0, column=0, sticky='w')
        Label(self.labFrame1, text="Sets:").grid(row=1, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1sets).grid(row=1, column=1)
        Label(self.labFrame1, text="Legs:").grid(row=2, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1legs).grid(row=2, column=1)
        Label(self.labFrame1, text="60+:").grid(row=3, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl160).grid(row=3, column=1)
        Label(self.labFrame1, text="80+:").grid(row=4, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl180).grid(row=4, column=1)
        Label(self.labFrame1, text="100+:").grid(row=5, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1100).grid(row=5, column=1)
        Label(self.labFrame1, text="140+:").grid(row=6, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1140).grid(row=6, column=1)
        Label(self.labFrame1, text="180:").grid(row=7, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1180).grid(row=7, column=1)
        Label(self.labFrame1, text="Averages").grid(row=8, column=0, sticky='w')
        Label(self.labFrame1, text="Score:").grid(row=9, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1avg).grid(row=9, column=1)
        Label(self.labFrame1, text="Checkout %:").grid(row=10, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1chtpc).grid(row=10, column=1)
        Label(self.labFrame1, text="Checkout Hit/Thrown:").grid(row=11, column=0, sticky='w')
        Label(self.labFrame1, textvariable=self.pl1chtnumbs).grid(row=11, column=1)


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
        Label(self.labFrame2, text="Totals").grid(row=0, column=0, sticky='w')
        Label(self.labFrame2, text="Sets:").grid(row=1, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2sets).grid(row=1, column=1)
        Label(self.labFrame2, text="Legs:").grid(row=2, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2legs).grid(row=2, column=1)
        Label(self.labFrame2, text="60+:").grid(row=3, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl260).grid(row=3, column=1)
        Label(self.labFrame2, text="80+:").grid(row=4, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl280).grid(row=4, column=1)
        Label(self.labFrame2, text="100+:").grid(row=5, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2100).grid(row=5, column=1)
        Label(self.labFrame2, text="140+:").grid(row=6, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2140).grid(row=6, column=1)
        Label(self.labFrame2, text="180:").grid(row=7, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2180).grid(row=7, column=1)
        Label(self.labFrame2, text="Averages").grid(row=8, column=0, sticky='w')
        Label(self.labFrame2, text="Score:").grid(row=9, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2avg).grid(row=9, column=1)
        Label(self.labFrame2, text="Checkout %:").grid(row=10, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2chtpc).grid(row=10, column=1)
        Label(self.labFrame2, text="Checkout Hit/Thrown:").grid(row=11, column=0, sticky='w')
        Label(self.labFrame2, textvariable=self.pl2chtnumbs).grid(row=11, column=1)

        #frame 3 widgets
        self.pl1remaining = StringVar()
        Label(self.labFrame3, text="Player:").grid(row=0, column=0)
        Label(self.labFrame3, textvariable=self.pl1name).grid(row=0, column=1)
        Label(self.labFrame3).grid(row=1)
        Label(self.labFrame3, text="Remaining").grid(row=2, column=0, columnspan=2, sticky='ew')
        self.remlabel1 = Label(self.labFrame3, textvariable=self.pl1remaining)
        self.remlabel1.grid(row=3, column=0, columnspan=2)
        self.remlabel1.configure(width=3,background='white', font=(None, 35))
        
        #self.pl1remaining.set(self.pl1dict['score'])
        #self.pl1name.set(game_state.player1)
        


        #frame 4 widgets
        self.pl2remaining = StringVar()
        Label(self.labFrame4, text="Player:").grid(row=0, column=0)
        Label(self.labFrame4, textvariable=self.pl2name).grid(row=0, column=1)
        Label(self.labFrame4).grid(row=1)
        Label(self.labFrame4, text="Remaining").grid(row=2, column=0, columnspan=2, sticky='ew')
        self.remlabel2 = Label(self.labFrame4, textvariable=self.pl2remaining)
        self.remlabel2.grid(row=3, column=0, columnspan=2)
        self.remlabel2.configure(width=3,background='white', font=(None, 35))
        #self.pl2remaining.set(self.pl2dict['score'])
        #self.pl2name.set(game_state.player2)

        #frame 5 widgets
        self.playertogo = StringVar()
        self.scoreEntered = StringVar()
        Label(self.labFrame5, text="    ").grid(row=0, column=0)
        #Label(labFrame5).grid(row=0, column=1)
        #Label(labFrame5).grid(row=0, column=2)
        Label(self.labFrame5, text="To Go:").grid(row=1, column=1)
        playerLabel = Label(self.labFrame5, textvariable=self.playertogo)
        playerLabel.grid(row=2, column=1)
        playerLabel.configure( font=(None, 20))
        
        self.number_entry = Entry(self.labFrame5, textvariable=self.scoreEntered, width=5)
        self.number_entry.grid(row=2, column=2)
        self.number_entry.configure(background='white', font=(None, 20))
        self.number_entry.focus()



    def start_window(self):

        
        self.startWindow = Toplevel(self.master)

        self.ply1entry = StringVar()
        self.ply2entry = StringVar()
        self.setsentry = StringVar()
        self.legsentry = StringVar()

        self.ply1Label = Label(self.startWindow, text="Player 1:")
        self.ply1Label.grid(row=3, column=3)
        self.ply1Entry = Entry(self.startWindow, textvariable=self.ply1entry, width=10)
        self.ply1Entry.grid(row=3, column=4, sticky='e')
        self.ply2Label = Label(self.startWindow, text="Player 2:")
        self.ply2Label.grid(row=4, column=3)
        self.ply2Entry = Entry(self.startWindow, textvariable=self.ply2entry, width=10)
        self.ply2Entry.grid(row=4, column=4, sticky='e')
        self.setsLabel = Label(self.startWindow, text="Number of Sets:")
        self.setsLabel.grid(row=5, column=3)
        self.setsBox = Combobox(self.startWindow, textvariable=self.setsentry, width=5)
        self.setsBox['values'] = ( 1, 3, 5, 7, 9)
        self.setsBox.current(1)
        self.setsBox.grid(row=5, column=4)
        self.legsLabel = Label(self.startWindow, text="Number of Legs:")
        self.legsLabel.grid(row=6, column=3)
        self.legsBox = Combobox(self.startWindow, textvariable=self.legsentry, width=5)
        self.legsBox['values'] = ( 1, 3, 5, 7, 9)
        self.legsBox.current(2)
        self.legsBox.grid(row=6, column=4)
        self.plyButton = Button(self.startWindow, text="Start Game", command=self.fiveohone_start)
        self.plyButton.grid(row=7, column=4)
        root.wait_window(self.startWindow)


    def fiveohone_start(self):
        player1name = self.ply1entry.get()
        player2name = self.ply2entry.get()
        numbersets = int(self.setsentry.get())
        numberlegs = int(self.legsentry.get())
        self.startWindow.destroy()



    def stats_update(self, player1, player2):

        
            

        self.pl1sets.set(player1.stats['sets'])
        self.pl1legs.set(player1.stats['legs'])
        self.pl1remaining.set(player1.stats['score'])
        self.pl160.set(player1.stats['60+'])
        self.pl180.set(player1.stats['80+'])
        self.pl1100.set(player1.stats['100+'])
        self.pl1140.set(player1.stats['140+'])
        self.pl1180.set(player1.stats['180'])
        numbset = ("%s / %s" % (player1.stats['dartsatdoubles'], player1.stats['doubleshit']))
        self.pl1chtnumbs.set(numbset)
        average1 = (player1.stats['totalScore']/player1.stats['numberDarts'])*3
        average1 = round(average1, 2)
        self.pl1avg.set(average1)
        
        #self.remlabel1.configure(background='yellow')
        #self.playertogo.set(self.player1name)
        
        self.pl2sets.set(player2.stats['sets'])
        self.pl2legs.set(player2.stats['legs'])
        self.pl2remaining.set(player2.stats['score'])
        self.pl260.set(player2.stats['60+'])
        self.pl280.set(player2.stats['80+'])
        self.pl2100.set(player2.stats['100+'])
        self.pl2140.set(player2.stats['140+'])
        self.pl2180.set(player2.stats['180'])
        self.pl2avg.set(player2.stats['avg'])
        numbset2 = ("%s / %s" % (player2.stats['dartsatdoubles'], player2.stats['doubleshit']))
        self.pl2chtnumbs.set(numbset2)
        average2 = (player2.stats['totalScore']/player2.stats['numberDarts'])*3
        average2 = round(average2, 2)
        self.pl2avg.set(average2)

        self.counter += 1


    def who_starts(self, sets, legs):
        
    

        if sets % 2 != 0:
            if legs % 2 != 0:
                self.playertogo.set(self.player1name)
                self.remlabel1.configure(background='yellow')
                self.remlabel2.configure(background='white')
                game_state.playertogo = 1
            else:
                self.playertogo.set(self.player2name)
                self.remlabel2.configure(background='yellow')
                self.remlabel1.configure(background='white')
                game_state.playertogo = 2
                

        

        

    

    def score_Entered(self):

        if self.counter == 1:
            player1.stats['totalScore'] = 0
            player1.stats['numberDarts'] = 0
        elif self.counter ==2:
            player2.stats['totalScore'] = 0
            player2.stats['numberDarts'] = 0


        self.score = int(self.scoreEntered.get())
        if game_state.playertogo == 1:
            player1.stats['score'] -= self.score
            player1.stats['totalScore'] += self.score
            player1.stats['numberDarts'] += 3
            player1.status(self.score, player1)
            self.stats_update(player1, player2)
            self.playertogo.set(self.player2name)
            self.remlabel2.configure(background='yellow')
            self.remlabel1.configure(background='white')
            if (player1.stats['score'] > 0) and (player1.stats['score']< 50):
                darts_at_double = Toplevel()
                self.doubleDarts = Combobox(darts_at_double, width=5, textvariable = self.dartsatdouble)
                self.doubleDarts.bind("<<ComboboxSelected>>", self.darts_at_double)
                self.doubleDarts['values'] = ('1', '2', '3')
                self.doubleDarts.grid(row= 1, column =1)
                main_app.wait_window(darts_at_double)
                #self.doubleDarts.grid()
                #self.doubleDarts_label.grid()
            self.number_entry.delete(0, END)
            game_state.playertogo = 2
        else:
            player2.stats['score'] -= self.score
            player2.stats['totalScore'] += self.score
            player2.stats['numberDarts'] += 3
            player2.status(self.score, player2)
            self.stats_update(player1, player2)
            self.playertogo.set(self.player1name)
            self.remlabel1.configure(background='yellow')
            self.remlabel2.configure(background='white')
            self.number_entry.delete(0, END)
            game_state.playertogo = 1




    def darts_at_double(self, player):
        self.darts_at_doubles = int(self.dartsatdouble.get())
        if game_state.playertogo == 2:
            player1.stats['dartsatdoubles'] += self.darts_at_doubles
        self.stats_update(player1, player2)
        self.doubleDarts.grid_remove()
        self.doubleDarts_label.grid_remove()



    def leg_won_darts(self):
        pass




class dartPlayer:

    def __init__(self):
        self.stats = {'sets': 0,
                      'legs': 0,
                      'score': 501,
                      '60+': 0,
                      '80+': 0,
                      '100+': 0,
                      '140+': 0,
                      '180': 0,
                      'avg': 0,
                      'totalScore': 1,
                      'numberDarts': 1,
                      'dartsatdoubles': 0,
                      'doubleshit':0}

    def status(self, score_entered, player):

        if score_entered == 180:
            player.stats['180'] += 1
        elif score_entered >= 140:
            player.stats['140+'] += 1
        elif score_entered >= 100:
            player.stats['100+'] += 1
        elif score_entered >= 80:
            player.stats['80+'] += 1
        elif score_entered >= 60:
            player.stats['60+'] += 1

class game:

    currentsets = 1
    currentlegs = 1
    playertogo = 0

    def setup(self, player1, player2, sets, legs):
        self.player1 = player1
        self.player2 = player2
        self.legs = legs
        self.sets = sets
            

        
    
               


player1 = dartPlayer()
player2 = dartPlayer()
game_state = game()
    
        



        

        


    

    
if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)
    
    root.mainloop()
