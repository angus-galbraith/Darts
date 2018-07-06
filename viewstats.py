from tkinter import*
import dartsdb
from tkinter.ttk import Treeview, Frame

class viewStats:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        #Frame.__init__(self, self.master)
        self.configure_gui1()
        self.create_widgets1()
        


    def configure_gui1(self):
        self.master.title("Statistics")
        self.master.geometry("400x400")



    def create_widgets1(self):

        #variables
        self.rtbhighestscores = StringVar()

        #padding
        Label(self.master).grid(row=0, column=0)
        Label(self.master).grid(row=0, column=1)
        

        #buttons
        Button(self.master, text="501", command=self.five_oh_one).grid(row=1, column=2)
        Button(self.master, text="Round the Board", command=self.round_the_board).grid(row=1, column=3)
        Button(self.master, text="Finishes", command=self.finishes).grid(row=1, column=4)
        Button(self.master, text="Cricket", command=self.cricket).grid(row=1, column=5)
        Button(self.master, text="View Stats", command=self.view_stats).grid(row=1, column=6)


    def five_oh_one(self):
        pass


    def round_the_board(self):
        #create treevie
        rtbtree = Treeview(self.master, columns=("highscore"))
        rtbtree.grid(row=3, column=3)
        rtbtree.heading("#0", text="Name")
        rtbtree.heading("#1", text="Score")
        rtbtree.column("#0", width=70)
        rtbtree.column("#1", width=40)
        rtbtree.column("#0", anchor='center')
        rtbtree.column("#1", anchor='center')
        

        
        rtb_highscores = []
        conn = dartsdb.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM rtb_highscores ORDER BY score DESC")
        while True:
            row =cursor.fetchone()
            if row is None:
                break
            rtbtree.insert("", index=END, text=row[0] , values=(row[1]))
        cursor.close()





    def finishes(self):
        pass


    def cricket(self):
        pass


    def view_stats(self):
        pass
