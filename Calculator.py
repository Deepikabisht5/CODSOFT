from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value= eval(screen.get())   

        scvalue.set(value)
        screen.update() 


    elif text== "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("400x650")
root.title("CALCULATOR")
root.configure(bg="light blue")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 20 bold")
screen.pack(fill=X ,ipadx=8,pady=8,padx=8)

f= Frame(root,bg="grey")
b = Button(f,text="9",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="grey")
b = Button(f,text="6",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="grey")
b = Button(f,text="3",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7,pady=10)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="grey")
b = Button(f,text="0",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7.75,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.75,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.75,pady=10)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="grey")
b = Button(f,text="*",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7.75,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.75,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.75,pady=10)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg="grey")
b = Button(f,text="C",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT ,padx=7.50,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.49,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx=15, pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=7.49,pady=10)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
