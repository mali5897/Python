from breezypythongui import EasyFrame

class SalaryGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Salary Demo", width = 340, height = 260, resizable = True)
        self.addLabel(text = "Please Enter your salary", row = 0, column = 0)
        self.addLabel(text = "what is the percentage of your raise each year?", row = 1, column = 0)
        self.addLabel(text = "How many years do you plan on staying?", row = 2, column = 0)
        self.salary = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)
        self.raiseAmnt = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
        self.years = self.addIntegerField(value = 0, row = 2, column = 1)
        self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
        self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)


    def compute(self):
        startingSal = self.salary.getNumber()
        rate = self.raiseAmnt.getNumber() / 100
        years = self.years.getNumber()
        if startingSal == 0 or rate == 0 or years == 0:
            return
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting Salary", "Raise", "Ending balance")
        totalRaiseAmnt = 0.0
        for year in range(1, years + 1):
            totalRaise = startingSal * rate
            endBalance = startingSal + totalRaise
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startingSal, totalRaise, endBalance)
            startingSal = endBalance
            totalRaiseAmnt += totalRaise
        result += "Ending balance: $%0.2f\n" % endBalance
        result += "Total raise amount earned: $%0.2f\n" % totalRaiseAmnt
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"

def main():
    SalaryGUI().mainloop()

if __name__ == "__main__":
    main()