from breezypythongui import EasyFrame
import math
class NumberFieldDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Number Field Demo", width = 540, height = 360, resizable = True)
        self.addLabel(text = "An integer", row = 0, column = 0)
        self.inputField = self.addIntegerField(value = 0, row = 0, column =1, width = 10)
        self.addLabel(text = "Square root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, precision = 2, state = "readonly")
        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)


    def computeSqrt(self):
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)
        

def main():
    NumberFieldDemo().mainloop()

if __name__ == "__main__":
    main() 