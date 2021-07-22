from tkinter import *
import os

root = Tk()
root.title("Kids Learning Kit")
root.geometry("1000x1000")
#--------------------------------------------------------------------------
menu = Menu(root)
root.config(menu = menu)
menu.add_cascade(label = "************************************************Click On Image for Tutorial************************************************")
#-------------------------------------------------------------------------
def TutorialFunction(event):
    os.system("tutorialVideo.mp4")
bgImage = PhotoImage(file = "KLKImage1.png")
tutorialButton = Button(root, image = bgImage, command = TutorialFunction)
tutorialButton.bind("<Button-1>", TutorialFunction)
tutorialButton.pack(side = TOP, fill = X)

def refrsh(event):
    os.system("E:/Python/PythonProject/TestPage.py")
refresh = Button(root, text = "Start")
refresh.bind("<Button-1>", refrsh)
refresh.pack(side = TOP)

root.mainloop()
