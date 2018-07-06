from tkinter import*
import dartsdb

class roundTheBoard:

    def __init__(self, master, playername):
        print(playername)
        self.playername = playername
        self.master = master
        self.frame = Frame(self.master)
        #Frame.__init__(self, self.master)
        self.configure_gui1()
        self.create_widgets()
        


    def configure_gui1(self):
        self.master.title("Round The Board")
        self.master.geometry("400x150")



    def create_widgets(self):

        # function binding return key to entry box
        self.master.bind('<Return>',lambda e:self.score_entered())


        #variables(stringvars)
        self.playerName = StringVar()
        self.numberToGoFor = StringVar()
        self.runningTotal = StringVar()
        self.scoreEntered =StringVar()
        self.finalMessage =StringVar()
        

        #variables
        self.number_to_go_for = 1
        self.total = 0
        self.numberToGoFor.set(self.number_to_go_for)
        self.runningTotal.set(0)




        #widgets

        #row0
        Label(self.master).grid()

        #row1
        Label(self.master, text="Player: ").grid(row=1, column=2)
        Label(self.master, textvariable=self.playerName).grid(row=1, column=4)
        self.playerName.set(self.playername)

        #row2
        Label(self.master).grid(row=2)

        #row3
        Label(self.master, text="Number to go for:").grid(row=3, column=1)
        Label(self.master, text="Number Hit:").grid(row=3, column=3)
        Label(self.master, text="Running Total:").grid(row=3, column=5)

        #row4
        self.scoreEntered = StringVar()
        Label(self.master, textvariable=self.numberToGoFor).grid(row=4, column=1)
        self.number_entry = Entry(self.master, textvariable=self.scoreEntered, width=10)
        self.number_entry.grid(row=4, column=3)
        self.number_entry.focus()
        Label(self.master, textvariable=self.runningTotal).grid(row=4, column=5)

        #row5
        Label(self.master).grid(row=5)


    def score_entered(self):

        self.number_entered = int(self.scoreEntered.get())
        self.throw_total = self.number_entered * self.number_to_go_for
        self.total += self.throw_total
        self.runningTotal.set(self.total)
        self.number_to_go_for += 1
        if self.number_to_go_for == 21:
            self.number_to_go_for = "Bulls "
            self.numberToGoFor.set(self.number_to_go_for)
            self.scoreEntered.set("")
            self.number_to_go_for = 25
        else:
            self.numberToGoFor.set(self.number_to_go_for)
            self.scoreEntered.set("")
        if self.number_to_go_for ==26:
            self.game_over(self.total)


    def game_over(self,final_total):
        self.finaltotal = final_total
        self.runningTotal.set(0)
        self.numberToGoFor.set(0)
        goLabel = Label(self.master, textvariable=self.finalMessage)
        goLabel.grid(row=6, column=2, columnspan=2)
        message = (" %s scored %d " % (self.playername, final_total))
        self.finalMessage.set(message)
        closeButton = Button(self.master, text="Continue", command=self.saveandclose)
        closeButton.grid(row=6, column=4)


    def saveandclose(self):
        conn = dartsdb.connect()
        cursor = conn.cursor()
        query = ("INSERT INTO rtb_highscores" "(name, score)" "VALUES ( %s, %s)")
        values = (self.playername, self.finaltotal)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        self.master.destroy()

        

    
        
        
