from tkinter import *
import random

attempts = 10 

answer = random.randint(1,100)
def check_answer():
    global attempts
    global text 

    attempts -=1

    guess = int(entry_window.get())

    if answer == guess:
        text.set("You win! Congrats!!")
        btn_check.pack_forget()

    elif attempts== 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()

    elif guess < answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Guess Higher ")

    elif guess > answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Guess Lower")

    return 


root = Tk()

root.title("Guess the number")
root.geometry("500x200")
root.configure(background="#FFD700")

label = Label(root, text="Guess the number between 1 & 100", font=('calibri', 16), bg="#FFD700")
label.pack()

entry_window = Entry(root, width=30, borderwidth=4, fg= "#000")
entry_window.pack()

btn_check = Button(root, text= "Check", command = check_answer, fg = 'black', bg = "#FFD700")
btn_check.pack()

btn_quit = Button(root, text="Quit", command = root.destroy, fg = 'black', bg = "#FFD700")
btn_quit.pack()


text = StringVar()
text.set("You have 10 attempts remaining! Good Luck!")


guess_attempts = Label(root, textvariable=text, font=('calibri', 14), fg = 'red', bg = "#FFD700")
guess_attempts.pack()

root.mainloop()
