
class SplitTips:
    def __init__(self, cash, ccards, open_tabs):
        self.cash = cash
        self.ccards = ccards
        self.open_tabs = open_tabs
        self.rolloverpercentage = self.open_tabs * .10

    def Split1(self):
        self.bartenders = int(input('Enter number of bartenders to split:    '))

        total = (self.cash + self.ccards + self.rolloverpercentage) / self.bartenders

        return total

    def Split2(self ):
        cash2 = self.cash - int(input("enter the amount of cash:  "))
        ccards2 = self.ccards - float(input("enter the amount of credit cards: "))
        opentabs2 = self.open_tabs - float(input("Enter the amount of open tabs:  "))
        self.rolloverpercentage = opentabs2 * .10
        self.cash = cash2
        self.ccards = ccards2
        self.open_tabs = opentabs2

##drive code
day1 = SplitTips(100, 50.25, 150.25)

# cash = int(input('Enter cash total:        '))
# ccards = float(input('Enter total cc tips:     '))
# open_tabs = float(input('Enter the total of open tabs:    '))

