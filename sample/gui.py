import tkinter


def play(start_hole, player, score_N, score_S,clicks):
    
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
                score_N = score_N + seeds[(start_hole + 1+ xx)%12]
            if player == 'S' : 
                score_S = score_S + seeds[(start_hole + 1+ xx)%12]
            seeds[(start_hole + 1+ xx)%12] = 0
    
    # display
    for idx in range(12):
        buttons[idx].config(text=seeds[idx])

     # update score
    scores[0].delete("1.0", "end")
    scores[0].insert('end',f'Score du Joueur N : {score_N}')
    scores[1].delete("1.0", "end")
    scores[1].insert('end',f'Score du Joueur S : {score_S}')


    # update click : 
    clicks += 1
    info[0].delete("1.0", "end")
    info[0].insert('end',f'nombre de click : {clicks}.')

    


def draw_board():
    # score box
    for idxs in range(2):
        score_box = tkinter.Text(
            root,
                height=2,
            width=73
            )
        score_box.pack(expand=True)
        if idxs == 0 : 
            score_box.place(x = 10 , y = 10)
            score_box.insert('end','Score du Joueur N : 0')
        if idxs == 1 :
            score_box.place(x = 10 , y = 250)
            score_box.insert('end','Score du Joueur S : 0')
        #score_box.config(state='disabled')
        scores.append(score_box)

        # info text

    info_box = tkinter.Text(
            root,
            height=2,
            width=73
            )
    info_box.pack(expand=True)
    info_box.place(x = 10 , y = 300)
    info_box.insert('end','Au tour du joueur S.')
    info.append(info_box)

    # holes
    for index_hole in range(12):
        button = tkinter.Button(
                    root, text = "4",  font=("Arial",10),
                    width=10,
                    height=5,
                    command =lambda idx = index_hole, ply = player,  sN = score_N, sS = score_S, ck = clicks: play(idx, ply, sN, sS,ck)
                    )
        button.pack(expand=True)
        if index_hole < 6:
            button.place(x= 10 + index_hole*100, y = 150)
        if index_hole > 5 : 
            button.place(x=  10 + 5*100 - (index_hole-6)*100 , y = 50)
        buttons.append(button)


# init 
buttons = []
scores = []
info = []
clicks = 0

player = 'S'
seeds = [4,4,4,4,4,4,4,4,4,4,4,4]
score_N = 0
score_S = 0
clicks = 0 

# creer la fenetre du jeu
root = tkinter.Tk()

#Personnalisation de la fenetre

root.title("Awale")
root.minsize(1000,500)
draw_board()

root.mainloop()