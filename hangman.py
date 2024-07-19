import random
from tkinter import *
from tkinter import messagebox


score = 0
run = True
b_g = '#000000' 
with open('words.txt','r') as f :
    words_len = len(f.readlines())


alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = [i for i in range(0,26)]
buttons = [[f"button{i+1}"] for i in range(0,26)]
for i in range(0,26) : 
    exec(f"buttons[{i}].extend([numbers[{i}]])")
    exec(f"buttons[{i}].extend([alpha[{i}]])")
    if i <= 12 :
        exec(f"buttons[{i}].extend([{i}*70,585])")
    else :
        exec(f"buttons[{i}].extend([({i}-13)*70,645]) ")

hangman_img = [f"h{i+1}" for i in range(0,7)]

hangman_label = [[f"hangman_label{i+1}",hangman_img[i]] for i in range(0,7)]

def replay(answer):
    global run,score
    if answer == True:
        run = True
        score = 0
        root.destroy()
    else:
        run = False
        root.destroy() 


while run:
    check_count = 0
    win_count = 0
    root = Tk()
    
    

    root.geometry('920x700')
    root.title('--HANG MAN--')
    root.config(bg = b_g)
   
    index = random.randint(0,853)
    with open('words.txt','r') as file:
        word_list = file.readlines()
    selected_word = word_list[index].strip('\n')
        
   
    x = 250
    for i in range(0,len(selected_word)):
        x += 50
        exec('d{}=Label(root,text="_",fg="#ffffff",bg="#000000",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))

    for number in numbers:
        exec('btn_img{}=PhotoImage(file="images/{}.png")'.format(number,number))
            
  
    for hangman in hangman_img:
        exec('{}=PhotoImage(file="images/{}.png")'.format(hangman,hangman))
            
    
    for button in buttons:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#000000",activebackground="#000000",font=10,image=btn_img{})'.format(button[0],button[2],button[0],button[1]))
        exec('{}.place(x={},y={})'.format(button[0],button[3],button[4]))
            
  
    for item in hangman_label:
        exec('{}=Label(root,bg="#000000",image={})'.format(item[0],item[1]))
        
    def close():
        global run
        answer = messagebox.askyesno('EXIT', 'DO YOU WANT TO EXIT THE GAME ? :(')
        if answer == True:
            run = False
            root.destroy()
      
    exit_img = PhotoImage(file = 'images/exit.png')
    exit_label = Button(root,bd = 0,command = close,bg="#999999",activebackground = "#999999",font = 0,image = exit_img,borderwidth=5,)
    exit_label.place(x=770,y=10)

    score = 'SCORE:'+str(score)
    score_label = Label(root,text = score,fg="#ffffff",bg = "#000000",font = ("arial",25))
    score_label.place(x = 10,y = 10)

    
    def check (letter,button):
        global check_count,win_count,run,score

        exec('{}.destroy()'.format(button))

        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 2
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                replay(answer)
        
        else:
            check_count += 1
            exec('hangman_label{}.place(x={},y={})'.format(check_count+1,300,100))
            if check_count == 6:
                answer = messagebox.askyesno('GAME OVER ', 'ANSWER : \''+selected_word.upper() +' \'\nYOU LOST! WANT TO PLAY AGAIN?')
                replay(answer)
                         
    root.mainloop()

