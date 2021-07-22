from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("KIDS LEARNING GAME")
root.geometry("500x750")
root.configure(bg='orange')
labely= Label(root, text="KIDS LEARNING GAME",borderwidth=7, relief="raised", bg="green", fg="white")
labely.pack(side = TOP)
labely.config(width=30)
labely.config(font=("Courier", 44))
labelx = Label(root, text = "Best of Luck", borderwidth=7, relief="raised", bg="green", fg="white")
labelx.pack(side = BOTTOM)
labelx.config(width=30)
labelx.config(font=("Courier", 44))
labelx.pack(side = BOTTOM)
topframe1=Frame(root)
topframe1.pack(side= TOP)
topframe = Frame(root)
topframe.pack(side = TOP)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

photo = PhotoImage(file ="testImage.png")
label = Label(topframe, image = photo)
label.pack(side = TOP)


alabel = Label(bottomframe, text = "   1.) ",  bg="black",fg="white")
blabel = Label(bottomframe, text = "   2.) ",  bg="black",fg="white")
clabel = Label(bottomframe, text = "   3.) ",  bg="black",fg="white")
dlabel = Label(bottomframe, text = "   4.) ",  bg="black",fg="white")
elabel = Label(bottomframe, text = "   5.) ",  bg="black",fg="white")
flabel = Label(bottomframe, text = "   6.) ",  bg="black",fg="white")

aEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
bEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
cEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
dEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
eEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
fEntry = Entry(bottomframe, width=50, bg="grey", fg="black")
alabel.grid(row = 0, sticky = E)
blabel.grid(row = 1, sticky = E)
clabel.grid(row = 2, sticky = E)
dlabel.grid(row = 3, sticky = E)
elabel.grid(row = 4, sticky = E)
flabel.grid(row = 5, sticky = E)

aEntry.grid(row = 0, column = 1)
bEntry.grid(row = 1, column = 1)
cEntry.grid(row = 2, column = 1)
dEntry.grid(row = 3, column = 1)
eEntry.grid(row = 4, column = 1)
fEntry.grid(row = 5, column = 1)

def sbmt(event, count=0):
    if (aEntry.get() == "Monkey" and
        bEntry.get() == "Squiril" and
        cEntry.get() == "Snake" and
        dEntry.get() == "Tortoise" and
        eEntry.get() == "Pig" and
        fEntry.get() == "Hippopotamus"):
        tkinter.messagebox.showinfo("Message", "All Answers Are Correct")
    if( aEntry.get() == "" or
        bEntry.get() == "" or
        cEntry.get() == "" or
        dEntry.get() == "" or
        eEntry.get() == "" or
        fEntry.get() == ""):
        tkinter.messagebox.showerror("Error", "Please Fill All the Boxes")
        breakpoint()
    if(aEntry.get() != "Monkey" ):
        count = count + 1
        
    if(bEntry.get() != "Squiril" ):
        
        count = count + 1
    if(cEntry.get() != "Snake" ):
        
        count = count + 1
    if(dEntry.get() != "Tortoise" ):
        
        count = count + 1
    if(  eEntry.get() != "Pig" ):
        
        count = count + 1
    if( fEntry.get() != "Hippopotamus"):
        
        count = count + 1
    tkinter.messagebox.showinfo("Message", "Submitted Successfully, "+str(count)+ " Answers Are Wrong")
def refrsh(event):
    if aEntry.get() or bEntry.get() or cEntry.get() or dEntry.get() or eEntry.get() or fEntry.get() is not None:
        aEntry.delete(0, "end")
        bEntry.delete(0, "end")
        cEntry.delete(0, "end")
        dEntry.delete(0, "end")
        eEntry.delete(0, "end")
        fEntry.delete(0, "end")
        aEntry.focus_set()
        
refresh = Button(topframe, text = "Refresh",bg="blue", fg="white")
refresh.bind("<Button-1>", refrsh)
refresh.pack(side = LEFT)


okButton = Button(topframe, text = "ok", bg="blue",fg="white")

okButton.bind("<Button-1>", sbmt)
okButton.pack(side = RIGHT)

def caseSens(event):
    tkinter.messagebox.showinfo("Case Sensitive", "All Answers are Case Sensitive So use Capitalized Form for Example- Lion, Tiger")

csinfo = Button(topframe, text = "All Answers are Case Sensitive, So use Capitalized Form",bg="red", fg="white")
csinfo.bind("<Button-1>", caseSens)
csinfo.pack()

root.mainloop()
