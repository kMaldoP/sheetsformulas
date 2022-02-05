
class SplitTips:
    def __init__(self, cash, ccards, open_tabs):
        self.cash = cash
        self.ccards = ccards
        self.open_tabs = open_tabs
        self.tippercentage = self.ccards * .10

    def split(self):
        self.bartenders = int(input('Enter number of bartenders to split:    '))

        total = (self.cash + self.ccards + self.tippercentage) / self.bartenders

        return total


##drive code
day1 = SplitTips(100, 50.25, 150.25)

# cash = int(input('Enter cash total:        '))
# ccards = float(input('Enter total cc tips:     '))
# open_tabs = float(input('Enter the total of open tabs:    '))

