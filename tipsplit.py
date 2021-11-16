
class split_tips:
    def __init__(self, cash, ccards, open_tabs):
        self.cash = cash
        self.ccards = ccards
        self.open_tabs = open_tabs
       

    def first_split(self):
        bartenders = int(input('Enter number of bartenders to split:    '))
        total1 = ((cash + ccards + (open_tabs * .10)) / bartenders)
        return total1



    

cash = int(input('Enter cash total:        '))
ccards =int(input('Enter total cc tips:     '))
open_tabs = int(input('Enter the total of open tabs:    '))
bartenders = int(input('Enter number of bartenders to split:    '))
