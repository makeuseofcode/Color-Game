from tkinter import *
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'White', 'Purple', 'Brown']
score = 0

time_remaining = 60

def beginGame(event):
    if time_remaining == 60:
        countdown()
    nextColour()

def nextColour():
    global score
    global time_remaining

    if time_remaining > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        timeLabel.config(text="Time left: " + str(time_remaining))
        timeLabel.after(1000, countdown)

root = Tk()
root.title("Color Game With a Twist")
root.geometry("750x450")
root.configure(background='Orange')
instructions = Label(root, text="Type the colour of the word not the text ;)", font=('Arial', 24), bg="orange")
instructions.pack()
scoreLabel = Label(root, text="Press Enter to begin", font=('Arial', 24), bg="orange")
scoreLabel.pack()

timeLabel = Label(root, text="Time remaining: " + str(time_remaining), font=('Arial', 24), bg="orange")
timeLabel.pack()
label = Label(root, font=('Arial', 90), bg="orange")
label.pack()
e = Entry(font=20)
root.bind('<Return>', beginGame)
e.pack()
e.focus_set()
root.mainloop()
