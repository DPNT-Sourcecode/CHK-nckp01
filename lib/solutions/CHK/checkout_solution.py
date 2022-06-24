import numpy as np
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
    a_tot = np.floor(a/3)*130+a%3 *50
    c_tot = c*20
    d_tot = d*15


