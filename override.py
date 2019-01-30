#overriding

class rbi:
    def createAccount(self):
        print("RBI:: account created")
    def processLoan(self):
        print("RBI:: rate of interest 10%")
    def __processPPF(self):
        print("RBI:: ppf rate 10.5%")
class hdfc(rbi):
    def demat(self):
        print("hdfc bank demat ")
    def processLoan(self):
        #create a new class
        rbi.processLoan(self)
        print('HDFC charges extra 5000')
        print("rate of interest of hdfc is:- 12%")
class sbi(rbi):
    def demat(self):
        print("sbi bank demat")

    def processLoan(self):
        rbi.processLoan(self)
        print('SBI charges 6000 extra')
        print("rate of interest of sbi is:- 13%")
class icici(rbi):
    def demat(self):
        print("icici bank demat")
    def processLoan(self):
        rbi.processLoan(self)
        print('icici 5000')
        print("rate of interest of icici is:- 14%")
h=hdfc()
h.createAccount()
h.processLoan()
h.demat()
s = sbi()
s.createAccount()
s.processLoan()
s.demat()
i = icici()
i.createAccount()
i.processLoan()
i.demat()