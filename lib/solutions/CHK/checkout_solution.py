
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    a = 0
    b = 0
    c = 0
    d = 0
    for letter in skus:
        if letter == 'A':
            a +=1
        elif letter == ' B':
            b +=1
        elif letter == ' C':
            c +=1
        elif letter == ' D':
            d +=1
        else:
            return -1
    

