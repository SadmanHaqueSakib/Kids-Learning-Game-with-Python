from tkinter import *
import os
import tkinter.messagebox
root = Tk()
root.title("Test Interface")
root.geometry("426x475")
labelx = Label(root, text = "Best of Luck")
labelx.pack(side = BOTTOM)

topframe = Frame(root)
topframe.pack(side = TOP)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

photo = PhotoImage(file ="testImage.png")
label = Label(topframe, image = photo)
label.pack(side = TOP)

def refrsh(event):
    os.system("tutorialVideo.mp4")
refresh = Button(topframe, text = "Tutorial")
refresh.bind("<Button-1>", refrsh)
refresh.pack(side = LEFT)

alabel = Label(bottomframe, text = "a.)")
blabel = Label(bottomframe, text = "b.)")
clabel = Label(bottomframe, text = "c.)")
dlabel = Label(bottomframe, text = "d.)")
elabel = Label(bottomframe, text = "e.)")
flabel = Label(bottomframe, text = "f.)")

aEntry = Entry(bottomframe)
bEntry = Entry(bottomframe)
cEntry = Entry(bottomframe)
dEntry = Entry(bottomframe)
eEntry = Entry(bottomframe)
fEntry = Entry(bottomframe)

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
    if (aEntry.get() != "Monkey" or
        bEntry.get() != "Squiril" or
        cEntry.get() != "Snake" or
        dEntry.get() != "Tortoise" or
        eEntry.get() != "Pig" or
        fEntry.get() != "Hippopotamus"):
        count = count + 1
        tkinter.messagebox.showinfo("Message", "Submitted Successfully, "+str(count)+ " Answers Are Wrong")

okButton = Button(topframe, text = "Submit")
okButton.bind("<Button-1>", sbmt)
okButton.pack(side = RIGHT)

def caseSens(event):
    tkinter.messagebox.showinfo("Case Sensitive", "All Answers are Case Sensitive So use Capitalized Form for Example- Lion, Tiger")

csinfo = Button(topframe, text = "All Answers are Case Sensitive, So use Capitalized Form")
csinfo.bind("<Button-1>", caseSens)
csinfo.pack()
root.mainloop()
