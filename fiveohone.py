from tkinter import *
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Combobox



class fiveOhOne:

    def __init__(self, master, player1name, player2name, numbersets, numberlegs):
        self.master = master
        self.frame = Frame(self.master)
        
        self.player1name = player1name
        self.player2name = player2name
        self.numbersets = numbersets
        self.numberlegs = numberlegs
        game_state.setup(self.player1name, self.player2name, self.numbersets, self.numberlegs)
        
        
    
        
        
        self.configure_gui1()
        self.who_starts(game_state.currentsets, game_state.currentlegs)
        #self.player_setup(player1name, player2name)
        self.counter  = 0
        self.stats_update(player1, player2)
        self.pl1avg.set(0)
        self.pl2avg.set(0)
        
        
        


    def configure_gui1(self):
        self.master.title("501")
        self.master.geometry("600x500")

        # function binding return key to entry box
        self.master.bind('<Return>',lambda e:self.score_Entered())

        #create frames
        labFrame1 = LabelFrame(self.master, text="Player1 Stats")
        labFrame2 = LabelFrame(self.master, text="Player2 Stats")
        labFrame3 = LabelFrame(self.master, text="Player1 Scores")
        labFrame4 = LabelFrame(self.master, text="Player2  Scores")
        labFrame5 = LabelFrame(self.master, text="Enter Scores")
        self.labFrame6 = LabelFrame(self.master, text="Additional info")

        #make frames vis(ible
        labFrame1.grid(row=0, column=0, rowspan=2, sticky='ns')
        labFrame3.grid(row=0, column=1)
        labFrame4.grid(row=0, column=2)
        labFrame2.grid(row=0, column=3, rowspan=2, sticky='ns')
        labFrame5.grid(row=1, column=1, columnspan=2, sticky='ew')
        self.labFrame6.grid(row=3, column=1, columnspan=2, sticky='ew')

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
        self.pl1name.set(game_state.player1)
        


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
        self.pl2name.set(game_state.player2)

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


        #frame6 widgets
        self.dartsatdouble= StringVar()
        self.legwondarts = StringVar()
        Label(self.labFrame6, text="    ").grid(row=0, column=0)
              
        self.doubleDarts = Combobox(self.labFrame6, width=5, textvariable = self.dartsatdouble)
        self.doubleDarts.bind("<<ComboboxSelected>>", self.darts_at_double)
        self.doubleDarts['values'] = ('1', '2', '3')
        self.doubleDarts.grid(row= 1, column =1)
        self.doubleDarts.grid_remove()
        self.doubleDarts_label = Label(self.labFrame6, text=' No of darts at double')
        self.doubleDarts_label.grid(row = 1, column =2)
        self.doubleDarts_label.grid_remove()
        self.legWon = Combobox(self.labFrame6, width=5, textvariable = self.legwondarts)
        self.legWon.bind("<<ComboboxSelected>>", self.leg_won_darts)

        
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
            if (player1.stats['score'] >= 0) and (player1.stats['score']< 50):
                self.dartsAtDouble = Toplevel()
                Label(self.dartsAtDouble, text="Darts at Double: ").grid(row=1, column=0)
                self.doubleDarts = Combobox(self.dartsAtDouble, width=5, textvariable = self.dartsatdouble)
                self.doubleDarts.bind("<<ComboboxSelected>>", self.darts_at_double)
                self.doubleDarts['values'] = ('0','1', '2', '3')
                self.doubleDarts.grid(row= 1, column =1)
                
                #root.wait_window(darts_at_double)
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
            if (player2.stats['score'] >= 0) and (player2.stats['score']< 50):
                self.dartsAtDouble = Toplevel()
                Label(self.dartsAtDouble, text="Darts at Double: ").grid(row=1, column=0)
                self.doubleDarts = Combobox(self.dartsAtDouble, width=5, textvariable = self.dartsatdouble)
                self.doubleDarts.bind("<<ComboboxSelected>>", self.darts_at_double)
                self.doubleDarts['values'] = ('0','1', '2', '3')
                self.doubleDarts.grid(row= 1, column =1)
            self.number_entry.delete(0, END)
            game_state.playertogo = 1




    def darts_at_double(self, player):

        self.legwondarts = StringVar()
        
        self.darts_at_doubles = int(self.dartsatdouble.get())
        if player1.stats['score'] == 0:
                    self.legWon = Toplevel()
                    Label(self.legWon, text="Darts Used: ").grid(row=1, column=0)
                    self.leg_won = Combobox(self.legWon, width=5, textvariable = self.legwondarts)
                    self.leg_won.bind("<<ComboboxSelected>>", self.leg_won_darts)
                    self.leg_won['values'] = ('1', '2', '3')
                    self.leg_won.grid(row= 1, column =1)
        if game_state.playertogo == 2:
            player1.stats['dartsatdoubles'] += self.darts_at_doubles
        else:
            player2.stats['dartsatdoubles'] += self.darts_at_doubles
        self.stats_update(player1, player2)
        self.dartsAtDouble.destroy()


    def leg_won_darts(self):
        pass


        
        
        


        #status(self.score, player)
        
        

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
    
