from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Label Demo", width = 240, height = 160, resizable = True, background = "orange")
        

def main():
    applicationName().mainloop()

if __name__ == "__main__":
    main()