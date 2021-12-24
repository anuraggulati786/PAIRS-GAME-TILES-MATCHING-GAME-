import random
import tkinter
from tkinter import messagebox, FALSE

root = tkinter.Tk()
root.title('PAIRS GAME')
root.geometry("530x560")

# for global winner we declare a counter
# set counteer variable to 0
winner = 0

# create our matches
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# shuffle our matches
random.shuffle(matches)
print(matches)

# create button frame

my_frame = tkinter.Frame(root)
my_frame.pack(pady=10)

# define some variable
count = 0
answer_list = []
answer_dict = {}


# Reset the game
def reset():
    global matches, winner
    winner = 0
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

    # shuffle our matches
    # random.shuffle(matches)
    # reset label

    my_label.config(text="")
    # reset our tiles
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]

    # we make a loop here for buttons and  change color's
    for button in button_list:
        button.config(text=" ", bg="SystemButtonFace", state="normal")


# defining our win function
def win():
    my_label.config(text="congratulations! you won")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]

    # we make a loop here for buttons and  change color's
    for button in button_list:
        button.config(bg="yellow")


# function for clicking buttons
def button_click(b, number):
    global count, answer_list, answer_dict, winner

    if b["text"] == " " and count < 2:
        b["text"] = matches[number]
        # add number to answer list
        answer_list.append(number)
        # add number to answer dictionary
        answer_dict[b] = matches[number]

        # incrementing our counter

        count += 1
        # answer _list return the positiion of the grid tabs that we clicked
        # print(answer_list)

        # start to determine correct or not
        if len(answer_list) == 2:
            if matches[answer_list[0]] == matches[answer_list[1]]:
                my_label.config(text="MATCH!")
                for key in answer_dict:
                    key["state"] = "disabled"
                count = 0
                answer_list = []
                answer_dict = {}

                # increment our winner counter
                winner += 1
                if winner == 6:
                    win()

            else:
                # my_label.config(text="OPPS?")
                count = 0
                answer_list = []
                # pop up box message box
                messagebox.showinfo("Incorrect", "Incorrect")

                # reset the buttons
                for key in answer_dict:
                    key["text"] = " "

                answer_dict = {}


# define our buttons

b0 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b0, 0),
                    relief="groove")
b1 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b1, 1),
                    relief="groove")
b2 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b2, 2),
                    relief="groove")
b3 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b3, 3),
                    relief="groove")
b4 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b4, 4),
                    relief="groove")
b5 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b5, 5),
                    relief="groove")
b6 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b6, 6),
                    relief="groove")
b7 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b7, 7),
                    relief="groove")
b8 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b8, 8),
                    relief="groove")
b9 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6, command=lambda: button_click(b9, 9),
                    relief="groove")
b10 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6,
                     command=lambda: button_click(b10, 10), relief="groove")
b11 = tkinter.Button(my_frame, text=" ", font=("helvetica,20"), height=3, width=6,
                     command=lambda: button_click(b11, 11), relief="groove")

# grid our buttons

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = tkinter.Label(root, text=" ")
my_label.pack(pady=20)

# here we created a menu 
my_menu = tkinter.Menu(root)
root.config(menu=my_menu)

# createed a dropdown menu option
option_menu = tkinter.Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game!", command=reset)
option_menu.add_separator()

option_menu.add_command(label="Exit Game!", command=root.quit)

root.mainloop()