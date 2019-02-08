from ExceptionHandling.Input import Input
from ExceptionHandling.validation import valid
class save:
    def __init__(self):
        Input.__init__(self)
        valid.__init__(self)
    def saveData(self):
        print('data save')
s =save()
s.saveData()