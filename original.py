#<------------------------------Modules------------------------------->
from tkinter import *
import pandas as pd                                                                                #libraries
import random

#<------------------------------Consonants---------------------------->
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('python/flash card for languages/data/Words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('python/flash card for languages/data/french_words.csv')                   #error handling
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
#<------------------------------Functions----------------------------->
#This function is used for to change the background,text,foreground color of text after the user has clicked on either wrong or correct button
def flip():
    canvas.itemconfig(card_title,text="English",fill = "white")
    canvas.itemconfig(card_word,text=current_card["English"],fill = "white")                              
    canvas.itemconfig(canvas_image,image=card_back)
#this will generate a card and after 3 sec it will call the flip function
def generate():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(card_title,text="French",fill = "black")
    canvas.itemconfig(card_word,text=current_card["French"],fill = "black")
    canvas.itemconfig(canvas_image,image=card_front)
    flip_timer=window.after(3000,flip)
#this will remove the words that i known from words to learn csv file so that i can focus on the words that i don't know
def unknown():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("python/flash card for languages/data/Words_to_learn.csv",index=False)
    generate()
#<------------------------------UI----------------------------------->
#UI making
window  = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip)
#canvas
canvas = Canvas(height = 526,width = 800,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="python/flash card for languages/images/card_front.png")
card_back = PhotoImage(file="python/flash card for languages/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.grid(row = 0,column=0,columnspan=2)
card_title = canvas.create_text(400,150,text="",font=("ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("ariel",60,"bold"))
#button
right = PhotoImage(file="python/flash card for languages/images/right.png")
button_right = Button(image=right,highlightthickness=0,command=generate)
button_right.grid(row=1,column=0)
wrong = PhotoImage(file="python/flash card for languages/images/wrong.png")
button_wrong = Button(image=wrong,highlightthickness=0,command=unknown)
button_wrong.grid(row=1,column=1)

generate()

window.mainloop()