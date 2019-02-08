def occurance():
    words = input('Enter some words:')
    d = set()
    for x in words:
       d = d.add(x) + 1
    for i in d:
        print(i)
occurance()