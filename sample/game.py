import random
import tkinter

class Awale :
    def __init__(self) :
        self.holes = []
        self.seeds = []
        self.score_N = 0
        self.score_S = 0


    def create_board(self) : 
        self.holes = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.seeds = [4,4,4,4,4,4,4,4,4,4,4,4]

    def create_scores(self) : 
        self.scores_N = 0
        self.scores_S = 0
    

    def get_random_first_player(self) :
        return random.randint(0, 1)

    def take_seeds(self, hole, player) :
        if player == 'N':
            start_hole = hole + 6 - 1
        
        if player == 'S' : 
            start_hole = hole - 1

        amount_seeds = self.seeds[start_hole]
        return start_hole, amount_seeds

    def move_seeds(self, start_hole, amount_seeds):

        self.seeds[start_hole] = 0
        for i in range(amount_seeds):
            self.seeds[(start_hole +1 +  i)%12] = self.seeds[(start_hole + +1 + i)%12] +1

        if self.seeds[start_hole] == 1 : 
            self.seeds[(start_hole + 1 +  amount_seeds )%12] = self.seeds[(start_hole + 1 +  amount_seeds )%12] + 1 
            self.seeds[start_hole] = 0
       

    def capture(self, start_hole, amount_seed, player):
        lasts =  range(amount_seed)[::-1] 
        for xx in lasts :  
            if (self.seeds[(start_hole + 1+ xx)%12]>3) | (self.seeds[(start_hole + 1+ xx)%12]<2):
                break
            if (self.seeds[(start_hole + 1+ xx)%12]==3) | (self.seeds[(start_hole + 1 + xx)%12]==2):
                if player == 'N':
                    self.score_N = self.score_N + self.seeds[(start_hole + 1+ xx)%12]
                if player == 'S' : 
                    self.score_S = self.score_S + self.seeds[(start_hole + 1+ xx)%12]
                self.seeds[(start_hole + 1+ xx)%12] = 0

    def is_player_win(self):
        win = False
        if self.score_N >= 24 :
            print("Le Joueur N a gagné !")
            win = True
        if self.score_S >= 24 : 
            print("Le joueur S a gagné ! ")
            win = True
        return win

    def swap_player_turn(self, player) :
        return 'N' if player == 'S' else 'S'


    def show_board(self) : 
        row_south = self.seeds[0:6]
        row_north = self.seeds[6:12][::-1]
        for item in row_north :
                print(item, "|",end=" ")
        print()
        for item in row_south :
            print(item, "|",end=" ")
        print()

    def show_scores(self) : 
        print("score joueur N : " , self.score_N )
        print("score joueur S : " , self.score_S )

    def check_total_seeds(self):
        seeds_on_board = 0
        for seed in self.seeds:
           seeds_on_board += seed
        total_seeds = self.score_N + self.score_S + seeds_on_board
        return total_seeds



    def start(self) :
        # initialisation
        self.create_board()
        self.create_scores()

        # Tirage du premier joueur
        player = 'N' if self.get_random_first_player() == 1 else 'S'

        # déroulement de la partie
        while True :
            self.show_board()
            self.show_scores()
            # prise en compte des données de l'utilisateur
            print( "C'est au tour du joueur", player,".")
            hole = int(input("Choisissez une case : "))
            print()
            # Prise des graine
            start_hole, amount_seeds = self.take_seeds(hole, player)
            # Déplacement
            self.move_seeds(start_hole,amount_seeds)
            # Capture
            self.capture(start_hole, amount_seeds, player)
            # Vérification fin de partie
            win = self.is_player_win()
            if win==True:
                break
            # Vérifiation nombre total de graines
            total_seeds = self.check_total_seeds()
            if total_seeds != 48:
                print("erreur total seeds")
                break
            # Joueur sivant
            player = self.swap_player_turn(player)

        self.show_board()
        self.show_scores()
# démarrer le jeu

root = tkinter.Tk()
root.title("Awale")
root.minsize(500,500)
root.mainloop()
awale = Awale()
awale.start()
