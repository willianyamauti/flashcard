
class Model:
    def __init__(self):
        self.db = 'data/to_learn.csv'
        self.card = Card_Model()


class Card_Model:
    def __init__(self):
        self.title = ''
        self.flip_title = ''
        self.word = ''
        self.flip_word = ''
        self.current = {}



