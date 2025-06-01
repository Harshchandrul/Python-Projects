from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------------------- FLIPPING CARDS ----------------------------- #
data = pandas.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')  # returns data dictionary in row format instead of column


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    # Checking if the words_current_card file exists
    if os.path.exists("words_to_learn.csv"):  # If it exists then we will choose from here
        new_data = pandas.read_csv('words_to_learn.csv')
        new_data_dict = new_data.to_dict(orient='records')
        current_card = random.choice(new_data_dict)
    else:
        current_card = random.choice(data_dict)

    canvas.itemconfig(french_text, text=current_card['French'], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(image_container, image=front_img)
    # Here i have to call flip card again after 3 sec
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(image_container, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(french_text, text=current_card['English'], fill="white")
    flip_timer = window.after(3000, next_card)


# ----------------------------- REMOVING LEARNED WORDS ----------------------------- #
def remove_word():
    global current_card, flip_timer
    print(current_card)
    data_dict.remove(current_card)
    #  It is showing error that data_dict is not in 
    x = pandas.DataFrame(data=data_dict)
    x.to_csv('words_to_learn.csv', index=False)
    next_card()


# ----------------------------- USER INTERFACE ----------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Card Images
front_img = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=535, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
image_container = canvas.create_image(400, 263, image=front_img)
# canvas.grid(column=0, row=0)
canvas.grid(column=0, row=0, columnspan=2)

french_text = canvas.create_text(
    400, 263,  # x and y coordinates of the text's center
    text="French",  # The text to display
    font=("Arial", 40, 'bold'),  # Font and size
    fill="black"  # Text color
)
title_text = canvas.create_text(
    400, 150,  # x and y coordinates of the text's center
    text="French",  # The text to display
    font=("Arial", 20, "italic"),  # Font and size
    fill="black"  # Text color
)

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=flip_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
