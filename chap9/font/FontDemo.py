from breezypythongui import EasyFrame
from tkinter.font import Font 

class FontDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Font Demo", width = 580, height = 440, resizable = True, background = "tomato")

        myFont = Font(size = 20, family = "Verdana", slant = "italic")
        
        
        self.addLabel(text = "Monday", row = 0, column = 0, background = "tomato", sticky = "ENSW", font = myFont)
        self.addLabel(text = "Tuesday", row = 0, column = 1, background = "tomato", sticky = "ENSW", font = myFont)
        self.addLabel(text = "Wednesday", row = 1, column = 0, background = "tomato", sticky = "ENSW", font = myFont)
        self.addLabel(text = "Thursday", row = 1, column = 1, background = "tomato", sticky = "ENSW")
        self.addLabel(text = "Hooray! It's Friday!", row =2 , column = 0, background= "tomato", columnspan = 2, sticky = "ENSW", font = Font(size = 16, family = "Impact"))


def main():
    FontDemo().mainloop()

if __name__ == "__main__":
    main()