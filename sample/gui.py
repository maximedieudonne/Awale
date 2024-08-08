import tkinter


def play(row, column):
    
    # get index hole
    if row == 0 : 
        start_hole = 5 - column + 6
    if row == 1 : 
        start_hole = column 
    
    # get amount_seeds
    amount_seeds = seeds[start_hole]
    # move
    seeds[start_hole] = 0
    for i in range(amount_seeds):
        seeds[(start_hole +1 +  i)%12] = seeds[(start_hole + +1 + i)%12] +1

    if seeds[start_hole] == 1 : 
        seeds[(start_hole + 1 +  amount_seeds )%12] = seeds[(start_hole + 1 +  amount_seeds )%12] + 1 
        seeds[start_hole] = 0
    
    # capture
    lasts =  range(amount_seeds)[::-1] 
    for xx in lasts :  
        if (seeds[(start_hole + 1+ xx)%12]>3) | (seeds[(start_hole + 1+ xx)%12]<2):
            break
        if (seeds[(start_hole + 1+ xx)%12]==3) | (seeds[(start_hole + 1 + xx)%12]==2):
            if player == 'N':
                score_N = self.score_N + seeds[(start_hole + 1+ xx)%12]
            if player == 'S' : 
                score_S = self.score_S + seeds[(start_hole + 1+ xx)%12]
            seeds[(start_hole + 1+ xx)%12] = 0
    


    # display
    order = [11,10,9,8,7,6,0,1,2,3,4,5]
    jj=-1
    for row in range(2):
        for column in range(6):
            jj=jj+1
            buttons[row][column].config(text=seeds[order[jj]])

    


def draw_board():
    for row in range(2):
        buttons_row = []
        for column in range(6):
            button = tkinter.Button(
                root, text = "4",  font=("Arial",10),
                width=20,
                height=10,
                command =lambda r=row,c=column: play(r,c)
                )
            button.grid(row = row, column = column)
            buttons_row.append(button)
        buttons.append(buttons_row)
    
    score_box = tkinter.Text(
        root,
        height=12,
        width=40
        )
    score_box.pack(expand=True)
    score_box.insert('end', "Score joueur N: ")
    score_box.config(state='disabled')


# stockage
buttons = []

# init 
seeds = [4,4,4,4,4,4,4,4,4,4,4,4]

# creer la fenetre du jeu
root = tkinter.Tk()

#Personnalisation de la fenetre

root.title("Awale")
root.minsize(500,500)
draw_board()
root.mainloop()