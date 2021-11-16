
class SplitTips:
    def __init__(self, cash, ccards, open_tabs):
        self.cash = cash
        self.ccards = ccards
        self.open_tabs = open_tabs
       

    def first_split(self):
        self.bartenders = int(input('Enter number of bartenders to split:    '))
        total1 = (self.cash + self.ccards + (self.open_tabs * .10) / self.bartenders)
        return total1


    

cash = int(input('Enter cash total:        '))
ccards = float(input('Enter total cc tips:     '))
open_tabs = float(input('Enter the total of open tabs:    '))

