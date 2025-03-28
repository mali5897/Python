"""
A prototype that lays out the user interface for a GUI-based guessing game.
"""
import random 
from breezypythongui import EasyFrame
class GuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = " Guessing Game", width = 500, height = 280)
        self.myNumber = random.randint(1, 100)
        self.count = 0 
        greeting = "Guess a number between 1 and 100."
        self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NEWS", columnspan = 2)
        self.addLabel(text= "Your guess", row = 1, column = 0)
        self.guessField = self.addIntegerField(0, row = 1, column = 1)
        self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
        self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)

    def nextGuess(self):
        self.count += 1
        guess = self.guessField.getNumber()
        if guess == self.myNumber:
            self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!"
            self.nextButton["state"] = "disabled"
        elif guess < self.myNumber:    
            self.hintLabel["text"] = "Sorry, too small!"
        else:
            self.hintLabel["text"] = "Sorry, too large!"


    def newGame(self):
        self.myNumber = random.randint(1, 100)
        self.count = 0 
        self.hintLabel["text"] = "Guess a number between 1 and 100."
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"





def main():
    GuessGame().mainloop()

if __name__ == "__main__":
    main()