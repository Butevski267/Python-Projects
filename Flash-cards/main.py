BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

current_card={}
dict={}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    dict = original_data.to_dict(orient='records')
    print(dict)
else:
    dict = data.to_dict(orient='records')
    print(dict)

# ------------------- Back End -------------------------------------------------

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    # Random dictionary
    current_card = random.choice(dict)
    canvas.itemconfig(card_image, image = front_image)
    canvas.itemconfig(card_title, text = 'French', fill='black')
    canvas.itemconfig(card_word, text = current_card['French'], fill='black')
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = 'English', fill='white')
    canvas.itemconfig(card_word, text = current_card['English'], fill='white')
    canvas.itemconfig(card_image, image= back_image)

def is_known():
    dict.remove(current_card)
    data_to_learn=pd.DataFrame(dict)
    data_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    next_card()

# ------------------- User Interface --------------------------------------------
window = Tk()
window.title('Flash Cards')
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

# Uploading images
back_image = PhotoImage(file='./images/card_back.png')
front_image = PhotoImage(file='./images/card_front.png')
correct_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

# Canvas
canvas = Canvas(width=800,height=560,highlightthickness=0,bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400,300, image = front_image)
canvas.grid(column=1,row=1,columnspan = 2)
# Canvas text
card_title = canvas.create_text(400, 150, text='French', font=('Ariel', 25, 'italic'))
current_card = random.choice(dict)
card_word = canvas.create_text(400, 280, text=current_card['French'], font=('Ariel', 32, 'bold'))

# Buttons
correct_button = Button(image=correct_image, highlightthickness=0,command = is_known)
correct_button.grid(column=2, row =2)

wrong_button = Button(image=wrong_image, highlightthickness=0,command = next_card)
wrong_button.grid(column=1, row =2)


window.mainloop()
