# creating our own iterator
class Alphabet():
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0
        return self
    
    def __next__(self):
        if self.index <= 25:
            char = self.letters[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

