from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


class View:
    def __init__(self,controller):
        self.controller = controller
        self.card = Card()
        self.panel = Panel(controller)


class Card:
    def __init__(self):
        self.canvas = Canvas(width=800, height=526, highlightthickness=0)
        self.img_front = PhotoImage(file="images/card_front.png")
        self.img_back = PhotoImage(file="images/card_back.png")
        self.card_image = self.canvas.create_image(400, 263, image=self.img_front)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)


class Panel:
    def __init__(self, controller):
        self.buttons_img_right = PhotoImage(file='images/right.png')
        self.buttons_img_wrong = PhotoImage(file='images/wrong.png')
        self.right_button = Button(image=self.buttons_img_right, highlightthickness=0, command=controller.view_got_right)
        self.wrong_button = Button(image=self.buttons_img_wrong, highlightthickness=0, command=controller.view_draw_card)
        self.right_button.grid(row=1, column=0, )
        self.wrong_button.grid(row=1, column=1, )
