from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Layout Demo", width = 480, height = 220, resizable = True, background = "tomato")

        self.addLabel(text = "Monday", row = 0, column = 0, background = "tomato", sticky = "ENSW")
        self.addLabel(text = "Tuesday", row = 0, column = 1, background = "tomato", sticky = "ENSW")
        self.addLabel(text = "Wednesday", row = 1, column = 0, background = "tomato", sticky = "ENSW")
        self.addLabel(text = "Thursday", row = 1, column = 1, background = "tomato", sticky = "ENSW")
        self.addLabel(text = "Hooray! It's Friday!", row =2 , column = 0, background= "tomato", columnspan = 2, sticky = "ENSW")


def main():
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()