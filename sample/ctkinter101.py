import tkinter as tk
import customtkinter as ctk
import PIL
import random

# color
SIENNA = "#A0522D"
SADDLEBROWN = "#8B4513"
BROWN = "#A52A2A"
SANDYBROWN = "#F4A460"
MAROON = "#800000"
WOOD = "#DEB887"
BURLYWOOD = "#DEB887"
LIGHTSTEELBLUE = "#B0C4DE"
# font
SEEDFONT = ("Helvetica", 30, "bold")

# background
image = PIL.Image.open("bg_awale.jpg")
background_image = ctk.CTkImage(image, size=(1350, 600))

# grid
LMARGIN = 30

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1350x800")
        self.title("Awale")
        
        self.make_GUI()

        self.start_game()

        self.mainloop()


    def  make_GUI(self):
                # background
        # Create a bg label
        bg_lbl = ctk.CTkLabel(self, image=background_image)
        bg_lbl.place(x=0, y=0)
        # make board
        self.board = ctk.CTkFrame(
            self,
            width = 1000,
            height = 400,
            fg_color = WOOD,
            
        )
        self.board.place(x = LMARGIN+150, y = 100)
        #self.board.place(relx = 0.5, rely = 0.5, anchor = "e")
        # make cells
        self.cells = []
        self.buttons = []
        for index_cell in range(12):
            cell_frame = ctk.CTkButton(
                    self.board,
                    width = 140,
                    height = 140,
                    text = "4",
                    corner_radius=60,
                    border_width=10,
                    fg_color = SIENNA,
                    border_color= MAROON,
                    text_color=SANDYBROWN,
                    font = SEEDFONT
                )
            if index_cell < 6:
                cell_frame.place(x= 50 + index_cell*150, y = 200)
            if index_cell > 5 : 
                cell_frame.place(x=  50 + 5*150 - (index_cell-6)*150 , y = 50)
            cell_frame.bind('<Button>', lambda event, idx=index_cell: self.play(event, idx))
            self.cells.append(cell_frame)

        # make score header Player North
        scoreN_frame = ctk.CTkFrame(self,
                                    width = 140,
                                    height = 400,
                                    fg_color = WOOD)
        scoreN_frame.place(x=LMARGIN, y = 100)
        self.scoreN_label = ctk.CTkLabel(
            scoreN_frame,
            text="Score N \n 0",
            font=SEEDFONT,
            text_color=BROWN
        )
        self.scoreN_label.place(relx = 0.5, rely=0.5, anchor = "center" )
        # make score header Player South
        scoreS_frame = ctk.CTkFrame(self,
                                    width = 140,
                                    height = 400,
                                    fg_color = WOOD)
        scoreS_frame.place(x=LMARGIN + 140 + 10 + 1000 + 10 , y = 100 )
        self.scoreS_label = ctk.CTkLabel(
            scoreS_frame,
            text="Score S \n 0",
            font=SEEDFONT,
            text_color=BROWN
        )
        self.scoreS_label.place(relx = 0.5, rely=0.5, anchor = "center" )

        # make player frame
        player_frame = ctk.CTkFrame(self,
                                    width = 10 + 140 + 10 + 1000  + 140,
                                    height = 140,
                                    fg_color = LIGHTSTEELBLUE)
        player_frame.place(x=LMARGIN,y = 620)
        self.player_label = ctk.CTkLabel(player_frame, text=" C'est au tour du joueur Sud", font=SEEDFONT)
        self.player_label.place(relx = 0.5, rely = 0.5, anchor = "center")



    # add methods to app

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
    app = App()
    app.mainloop()