from tkinter import *
from view import View
from model import Model
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


class Controller:
    def __init__(self):
        self.root = Tk()
        # self.model = Model()
        self.view = View(self)
        self.model = Model()
        self.root.title("FlashCard")
        self.word_dict = self.model_build_words_dict()
        self.root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        # self.timer = None
        self.view_create_card()
        self.timer = self.root.after(3000, func=self.view_flip_card)
        self.root.mainloop()

    # ************** Model related methods **************

    def model_build_data_frame(self):
        data = pd.read_csv(self.model.db)
        return data

    def model_build_words_dict(self):
        try:
            data_frame = self.model_build_data_frame()
        except FileNotFoundError:
            self.model.db = 'data/french_words.csv'
            original_data = self.model_build_data_frame()
            to_learn = original_data.to_dict(orient="records")
        else:
            to_learn = data_frame.to_dict(orient="records")

        return to_learn

    def model_generate_new_card(self):
        new_card = choice(self.word_dict)
        # atribute the values from new card
        self.model.card.title, self.model.card.flip_title = new_card.keys()
        self.model.card.word, self.model.card.flip_word = new_card.values()
        self.model.card.current = new_card

    # ************** View related methods **************

    def view_create_card(self):
        self.model_generate_new_card()
        self.view.card.canvas.itemconfig(self.view.card.card_image, image=self.view.card.img_front)
        self.view.card.canvas.itemconfig(self.view.card.card_title, text=self.model.card.title, fill='black')
        self.view.card.canvas.itemconfig(self.view.card.card_word, text=self.model.card.word, fill='black')

    def view_flip_card(self):
        self.view.card.canvas.itemconfig(self.view.card.card_image, image=self.view.card.img_back)
        self.view.card.canvas.itemconfig(self.view.card.card_title, text=self.model.card.flip_title, fill='white')
        self.view.card.canvas.itemconfig(self.view.card.card_word, text=self.model.card.flip_word, fill='white')

    def view_draw_card(self):
        self.root.after_cancel(self.timer)
        self.view_create_card()
        self.timer = self.root.after(3000, func=self.view_flip_card)

    def view_got_right(self):
        self.word_dict.remove(self.model.card.current)
        new_df = pd.DataFrame(self.word_dict)
        new_df.to_csv("data/words_to_learn.csv", index=False)
        self.view_draw_card()

    # def view_got_wrong(self):
    #     self.view_draw_card()


