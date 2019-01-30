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
class sbi(rbi):
    def demat(self):
        print("sbi bank demat")
class icici(rbi):
    def demat(self):
        print("icici bank demat")
s = sbi()
h = hdfc()
i = icici()
s.createAccount()
s.processLoan()
s.demat()
h.createAccount()
h.processLoan()
h.demat()
i.createAccount()
i.processLoan()
i.demat()
