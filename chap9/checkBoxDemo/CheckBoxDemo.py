from breezypythongui import EasyFrame
from tkinter.font import Font

class CheckBoxDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Check Box Demo", width = 320, height = 200, resizable = True, background = "#A3C9A8")
        self.addLabel(text = "Today's Menu", row = 0, column = 0, sticky = "NEWS", background = "#A3C9A8", foreground = "black", font = Font(size = 26, family = "Elephant"))
        self.chickCB = self.addCheckbutton(text = "Chicken", row = 0, column = 0)
        self.taterCB = self.addCheckbutton(text = "French fries", row = 0, column = 1)
        self.beanCB = self.addCheckbutton(text = "Green beans", row = 1, column = 0)
        self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 1, column = 1)
        self.addButton(text = "Place order", row = 2, column = 0, columnspan = 2, command = self.placeOrder)

    def placeOrder(self):
        message = ""
        if self.chickCB.isChecked():
            message += "Chicken\n\n"
        if self.taterCB.isChecked():
            message += "French fries\n\n"
        if self.beanCB.isChecked():
            message += "Green beans\n\n"
        if self.sauceCB.isChecked():
           message += "Applesauce\n"
        if message == "":
            message = "No food ordered!"
        self.messageBox(title = "Customer Order", message = message)
        
def main():
    CheckBoxDemo().mainloop()

if __name__ == "__main__":
    main()