# This script creates a basic GUI

# imports
import tkinter as tk


# constants

# screen dimentions
WIDTH = 500
HEIGHT = 700

# GUI elemnts
myfont = ('Microsoft YaHei Light', '20')  # font face and size
buttonfont = ('Microsoft YaHei Light', '15')
titlefont = ('Microsoft YaHei Light', '50')
BG = '#330066'


def buttonPressed(p1Entry, p2Entry, p1, p2, root):
    if len(p1Entry.get()) > 0:
        p1.name = p1Entry.get()
    if len(p2Entry.get()) > 0:
        p2.name = p2Entry.get()
    root.destroy()  # gets rid of the GUI terminal


def draw(root, p1, p2):
    # all the gui elemnts drawn here
    # the background color
    bgCol = tk.Label(root, bg=BG)
    bgCol.place(relheight=1, relwidth=1)

    # title of the game
    titleFrame = tk.Frame(root, bg=BG)  # creating a frame to hold the game title
    titleFrame.place(relwidth=1, relheight=0.3)
    gameTitle = tk.Label(titleFrame, bg=BG, fg='white', text='Air Hockey', font=titlefont)
    gameTitle.place(relx=0.17, rely=0.2)
    author = tk.Label(titleFrame, bg=BG, fg='white', text='sed cat', font=myfont)
    author.place(relx=0.4, rely=0.65)

    # player name input
    playerFrame = tk.Frame(root, bg=BG)
    playerFrame.place(relwidth=1, relheight=0.65, rely=0.35)

    p1name = tk.Label(playerFrame, bg=BG, fg='white', text='PLayer 1 Name: ', font=myfont)
    p1name.place(relx=0.1, rely=0.1)
    p1Entry = tk.Entry(playerFrame)
    p1Entry.place(rely=0.123, relx=0.5, relwidth=0.4, relheight=0.055)

    p2name = tk.Label(playerFrame, bg=BG, fg='white', text='PLayer 2 Name: ', font=myfont)
    p2name.place(relx=0.1, rely=0.3)
    p2Entry = tk.Entry(playerFrame)
    p2Entry.place(rely=0.323, relx=0.5, relwidth=0.4, relheight=0.055)

    # buttons
    playButton = tk.Button(playerFrame, text='Play', font=buttonfont, command=lambda: buttonPressed(p1Entry, p2Entry, p1, p2, root))
    playButton.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)


def mainLoop(p1, p2):
    # .......the main GUI loop starts here.......
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # whatever is written between this is gonna be in the gui

    root = tk.Tk()  # creating a root as the main body of the GUI

    # canvas to hold the shape of GUI by drawing a rectangle
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

    draw(root, p1, p2)

    canvas.pack()

    root.mainloop()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
