from tkinter import *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(background="#cdb4db")

rock_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_c.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_c.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_c.png"))

#insert picture
user_label = Label(root,image=scissor_img, bg="#cdb4db")
comp_label = Label(root,image=scissor_img_comp,bg="#cdb4db")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root, text=0, font= 100,bg="#cdb4db", fg="white")
computerScore = Label(root, text=0, font= 100,bg="#cdb4db", fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator= Label(root, font=50,text="USER",bg="#cdb4db")
comp_indicator= Label(root, font=50,text="COMPUTER",bg="#cdb4db")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50,bg="#cdb4db",fg="black")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score =int(playerScore["text"])
    score+=1
    playerScore["text"] = str(score)

#update computer score
def updateComputerScore():
    score =int(computerScore["text"])
    score+=1
    computerScore["text"] = str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("Its a Tie!!!")
    elif player=="rock":
        if computer=="paper":
            updateMessage("You Lose!!!")
            updateComputerScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore
    elif player=="paper":
        if computer=="scissor":
            updateMessage("You Lose!!!")
            updateComputerScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("You Lose!!!")
            updateComputerScore
        else:
            updateMessage("You Win!!!")
            updateUserScore
    else:
        pass

#update choices
choices = ["rock","paper","scissor"]
def updateChoice(x):
#for computer
    compChoice= choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif x=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

#Buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#0077b6", fg="black",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#ff0054", fg="black",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#e09f3e", fg="black",command=lambda:updateChoice("scissor")).grid(row=2,column=3)



root.mainloop()

 