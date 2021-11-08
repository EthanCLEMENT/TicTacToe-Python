import tkinter as tk
import numpy as np
import Bot

def circle(x,y):
    canvas.create_oval(x+10,y+10,x+100-10,y+100-10,outline="red",width=3)
    
def cross(x,y):
    canvas.create_line(x+10,y+10,x+100-10,y+100-10,fill="blue",width=3)
    canvas.create_line(x+10,y+100-10,x+100-10,y+10,fill="blue",width=3)
    
def click(event):
    global ans
    row, column=square(event.x,event.y)
    x,y = coordinates(row,column)
    if board[row,column]==0:
        if ans%2==0:
            cross(x,y)
            board[row,column]=1
            txtplayer="Cross"
        else:
            circle(x,y)
            board[row,column]=2
            txtplayer="Circle"
        if win(row,column):
            labelwin.config(text=txtplayer+" won !")
            canvas.unbind("<Button-1>")
        elif ans == 8:
            labelwin.config(text="Tie")
        ans+=1
        
def square(x,y):
    if x<100:
        column = 0
    elif x<200:
        column=1
    else:
        column=2
    if y<100:
        row=0
    elif y<200:
        row=1
    else:
        row=2
    return(row, column)

def coordinates(row, column):
    if column == 0:
        x=0
    elif column == 1:
        x=100
    else:
        x=200
    if row == 0:
        y=0
    elif row == 1:
        y=100
    else:
        y=200
    return(x,y)

def win(row,column):
    if board[row,0] == board[row,1] == board[row,2]:
        return True    
    if board[0,column] == board[1,column] == board[2,column]:
        return True
    if board[0,0] == board[1,1] == board[2,2]!=0:
        return True
    if board[0,2] == board[1,1] == board[2,0]!=0:
        return True
    return False
        
#define window
window = tk.Tk()

#grill 3*3
canvas = tk.Canvas(window, width=300, height=300, background="white")
canvas.create_line(100,0,100,300, width = 3, fill="black")
canvas.create_line(200,0,200,300,width = 3, fill="black")
canvas.create_line(0,100,300,100, width = 3, fill="black")
canvas.create_line(0,200,300,200, width = 3, fill="black")
canvas.grid()

#label
labelwin = tk.Label(window, text=" ")
labelwin.grid()

#mouse binding
canvas.bind("<Button-1>", click)

#board
board=np.zeros((3,3))

#variable
ans = 0 

tk.mainloop()