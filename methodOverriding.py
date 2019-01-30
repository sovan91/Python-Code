# if child is not satisfied with parent properties then child has create has own property. this concept is call overriding
# for overriding method name and method signature are same
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
        print("rate of interest of hdfc is:- 12%")
class sbi(rbi):
    def demat(self):
        print("sbi bank demat")

    def processLoan(self):
        print("rate of interest of sbi is:- 13%")
class icici(rbi):
    def demat(self):
        print("icici bank demat")
    def processLoan(self):
        print("rate of interest of icici is:- 14%")
r = rbi()
r.createAccount()
r.processLoan()
s=sbi()
s.processLoan()
s.demat()
h= hdfc()
h.processLoan()
h.demat()
i = icici()
i.processLoan()
i.demat()


