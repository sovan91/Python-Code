def search():
    list1 = ['sovan','shyamal','sayan',',madhu','satya']
    src = str(input('enter the search string:'))
    for names in list1:
        if src == list1[names]:
            print(src)
        else:
            print('serach string is not found')
search()
