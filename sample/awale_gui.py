import tkinter as tk
import random


FONT = ("Helvetica", 30, "bold")
SEED_FONT = ("Helvetica", 10, "bold")
BG_COLOR = "#add8e6"
BOARD_COLOR = "#65000b"
CELL_COLOR = "#e1ad21"


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Awale")
        self.main_grid = tk.Frame(
            self, bg =BG_COLOR, bd=3,
            width = 1000, height=1000
        )

        self.main_grid.grid()
        
        self.make_GUI()

        self.start_game()

        self.mainloop()
        
    def make_GUI(self):
        # make board
        self.board = tk.Frame(
            self.main_grid, bg =BOARD_COLOR,
            width = 900, height=350
        )
        self.board.place(x = 10, y = 100)

        # make cells
        self.cells = []
        self.buttons = []
        for index_cell in range(12):
            # frame
            cell_frame = tk.Button(
                    self.board,
                    bg=CELL_COLOR,
                    text = "4",
                    font = SEED_FONT,
                    width = 10,
                    height = 5,
                )
            if index_cell < 6:
                cell_frame.place(x= 10 + index_cell*150, y = 200)
            if index_cell > 5 : 
                cell_frame.place(x=  10 + 5*150 - (index_cell-6)*150 , y = 50)
            cell_frame.bind('<Button>', lambda event, idx=index_cell: self.play(event, idx))
            self.cells.append(cell_frame)
            
        
        # make score header Player North
        scoreN_frame = tk.Frame(self)
        scoreN_frame.place(relx=0.5, y = 45, anchor = "center")
        tk.Label(
            scoreN_frame,
            text="Score Player North",
            font=FONT
        ).grid(row=0)
        self.scoreN_label = tk.Label(scoreN_frame, text="0", font=FONT)
        self.scoreN_label.grid(row=1)

        # make score header player South
        scoreS_frame = tk.Frame(self)
        scoreS_frame.place(relx=0.5,y = 520, anchor = "center")
        tk.Label(
            scoreS_frame,
            text="Score Player South",
            font=FONT
        ).grid(row=0)
        self.scoreS_label = tk.Label(scoreS_frame, text="0", font=FONT)
        self.scoreS_label.grid(row=1)

        # make player frame
        player_frame = tk.Frame(self)
        player_frame.place(x=5,y = 620)
        tk.Label(
            player_frame,
            text="C'est au tour du joueur ",
            font=FONT
        ).grid(row = 0, column=0)
        self.player_label = tk.Label(player_frame, text="Sud", font=FONT)
        self.player_label.grid(row = 0, column=1)

        # make win frame
        win_frame = tk.Frame(self)
        win_frame.place(x=5,y = 720)
        self.win_label = tk.Label(win_frame, text="", font=FONT)
        self.win_label.grid()


    def start_game(self):
        self.seeds = [4,4,4,4,4,4,4,4,4,4,4,4]
        self.taken_seed = 0
        self.scoreN = 0
        self.scoreS = 0
        self.player = 'S'
        self.flag_correct_move = True
    

    def get_random_first_player(self) :
        return random.randint(0, 1)


    def take_seed(self, idx_cell):
        self.flag_correct_move = True
        if (self.player == 'N') & (idx_cell>=0) & (idx_cell<=5):
            self.flag_correct_move = False
        if (self.player == 'S') & (idx_cell>=6) & (idx_cell<=11):
            self.flag_correct_move = False
        if  self.seeds[idx_cell]  == 0 :
            self.flag_correct_move = False


    def move_seeds(self, idx_cell):
        #move
        amount_seeds = self.seeds[idx_cell]
        self.seeds[idx_cell] = 0
        for i in range(amount_seeds):
            self.seeds[(idx_cell +1 +  i)%12] = self.seeds[(idx_cell + +1 + i)%12] +1

        if self.seeds[idx_cell] == 1 : 
            self.seeds[(idx_cell + 1 +  amount_seeds )%12] = self.seeds[(idx_cell + 1 +  amount_seeds )%12] + 1 
            self.seeds[idx_cell] = 0
       

        # capture
        lasts =  range(amount_seeds)[::-1] 
        for xx in lasts :  
            if self.player=='N':
                if (self.seeds[(idx_cell  + xx +1 )%12]>3) | (self.seeds[(idx_cell  + xx +1 )%12]<2):
                    break
                if (self.seeds[(idx_cell  + xx +1 )%12]==3) | (self.seeds[(idx_cell  + xx +1 )%12]==2):
                    if ((idx_cell  + xx +1 )%12 <= 5) & ((idx_cell  + xx +1 )%12 >=0 ):
                        self.scoreN = self.scoreN + self.seeds[(idx_cell  + xx +1)%12]
                        self.seeds[(idx_cell  + xx +1 )%12] = 0
            if self.player=='S':
                if (self.seeds[(idx_cell  + xx +1 )%12]>3) | (self.seeds[(idx_cell  + xx +1 )%12]<2):
                    break
                if (self.seeds[(idx_cell  + xx +1 )%12]==3) | (self.seeds[(idx_cell  + xx +1 )%12]==2):
                    if ((idx_cell  + xx +1 )%12 <= 11) & ((idx_cell  + xx +1 )%12 >=6 ):
                        self.scoreS = self.scoreS + self.seeds[(idx_cell  + xx +1)%12]
                        self.seeds[(idx_cell  + xx +1 )%12] = 0




    def is_player_win(self):
        win = False
        if self.scoreN >= 24 :
            self.win_label.config(text="Le Joueur N a gagné !")
            win = True
        if self.scoreS >= 24 : 
            self.win_label.config(text="Le Joueur S a gagné !")
            win = True
        return win

    def swap_player_turn(self) :
        pl = 'N' if self.player == 'S' else 'S'
        print(pl)
        return pl
    

    def update_GUI(self):
        for idx in range(12):
            self.cells[idx].config(text=self.seeds[idx])
        
        self.scoreN_label.config(text=self.scoreN)
        self.scoreS_label.config(text=self.scoreS)

        if self.player == 'S' :
            self.player_label.config(text = " Sud ")
        if self.player == 'N' :
            self.player_label.config(text = " Nord ")

    def play(self,event, idx_cell):
        self.take_seed(idx_cell)
        if self.flag_correct_move : 
            self.move_seeds(idx_cell)
            self.player = self.swap_player_turn()
            self.update_GUI()
            self.is_player_win()

if __name__ == "__main__":
    Game()