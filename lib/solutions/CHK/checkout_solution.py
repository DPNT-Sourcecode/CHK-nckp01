import string

import numpy as np
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    alphabet_count = np.zeros(26)
    # Get total number of each amount
    for letter_ind in range(string.ascii_uppercase):
        alphabet_count[letter_ind] = skus.count(string.ascii_uppercase[letter_ind])
    if not skus.isupper():
        return -1


    # Calculate totals for each
    b = b - np.floor(e/2) # Remove free ones from deal with E
    if b<0:
        b= 0
    # get number of complete sets of 5 and add deal, get remainder to calculate total of deal with 3, then remainder to
    # calculate total
    a_tot = np.floor(a/5)*200 + np.floor((a%5)/3)*130+ ((a%5) % 3) * 50
    # get number of complete sets of 2 and add deal, get remainder to calculate total
    b_tot = np.floor(b/2)*45 + b % 2 * 30
    c_tot = c*20
    d_tot = d*15
    e_tot = e*40
    f_tot = np.floor(f/3)*20 + f % 3 *10

    total = a_tot+b_tot+c_tot+d_tot+e_tot+f_tot

    return total

