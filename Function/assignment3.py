uid = int(input('enter user id:'))
uage = int(input('enter user age:'))
def validation():
    if uid < 0 or uage < 18 :
        print('condition must not matched...')
    else:
      def id():
        print('user id is:',uid)
      id()
      def age():
        print('enter user age is:',uage)
        return

      age()
validation()