from tkinter import *
import pandas
import random

from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv("data/to_learn.csv")
except (FileNotFoundError,EmptyDataError):
    data=pandas.read_csv("data/french-english.csv")
file_to_dict=data.to_dict(orient="records")
flip_timer=None
current_hold={}

def next_card():
    global current_hold,flip_timer
    window.after_cancel(flip_timer)
    current_hold=random.choice(file_to_dict)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_hold["French"],fill="black")
    canvas.itemconfig(front,image=img_front)
    flip_timer=window.after(4000, flip)


def flip():
    global current_hold

    canvas.itemconfig(front,image=img_back)
    canvas.itemconfig(card_title,text="English", fill="#FFFFFF")
    canvas.itemconfig(card_word,text=current_hold["English"], fill="#FFFFFF")


def is_known():
    file_to_dict.remove(current_hold)
    data=pandas.DataFrame(file_to_dict)
    data.to_csv("data/to_learn.csv",index=False)
    next_card()

window=Tk()
window.config(bg=BACKGROUND_COLOR,pady=20,padx=50)
window.title("Flash-Card")
flip_timer=window.after(4000,flip)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
img_front=PhotoImage(file="images/card_front.png")
img_back=PhotoImage(file="images/card_back.png")
front=canvas.create_image(415,275,image=img_front)
card_title=canvas.create_text(400,100,text="Title",font=("OCR A Extended",50,"italic"))
card_word=canvas.create_text(400,300,text="Word",font=("Courier",80,"bold"))
canvas.grid(row=1,column=1)


label=Label(text="Do you know what this word means?",font=("OCR A Extended",40,"bold"),bg=BACKGROUND_COLOR)
label.grid(row=2,column=1)
img_wrong=PhotoImage(file="images/wrong.png")
button_wrong=Button(image=img_wrong,width=60,height=60,command=next_card)
button_wrong.grid(row=3,column=0)
img_right=PhotoImage(file="images/right.png")
button_right=Button(image=img_right,width=60,height=60,command=is_known)
button_right.grid(row=3,column=2)

next_card()
window.mainloop()
