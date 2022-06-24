import string

import numpy as np
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    counts = np.zeros(26)
    if len(skus) == 0:
        return 0
    if len(skus[0]) == 0:
        return 0
    if not skus.isupper() or not skus.isalpha():
        return -1
    # Get total number of each amount

    for letter_ind in range(len(string.ascii_uppercase)):
        counts[letter_ind] = skus.count(string.ascii_uppercase[letter_ind])

    # Calculate totals for each
    # Remove free buy nx get y free deal
    counts[1] = counts[1] - np.floor(counts[4]/2)
    if counts[1]<0:
        counts[1]= 0
    counts[12] = counts[12] - np.floor(counts[13]/3)
    if counts[12]<0:
        counts[12]= 0
    counts[16] = counts[16] - np.floor(counts[17]/3)
    if counts[16]<0:
        counts[16]= 0

    counts[0] = np.floor(counts[0]/5)*200 + np.floor((counts[0]%5)/3)*130+ ((counts[0]%5) % 3) * 50
    counts[1] = np.floor(counts[1]/2)*45 + counts[1] % 2 * 30
    counts[2] = counts[2]*20
    counts[3] = counts[3]*15
    counts[4] = counts[4]*40
    counts[5] = np.floor(counts[5]/3)*20 + counts[5] % 3 *10
    counts[6] = counts[6]*20
    counts[7] = np.floor(counts[7]/10)*80 + np.floor((counts[7]%10)/5)*45+ ((counts[7]%10) % 5) * 10
    counts[8] = counts[8]*35
    counts[9] = counts[9]*60
    counts[10] = np.floor(counts[10]/2)*120 + counts[10] % 2 * 70
    counts[11] = counts[11]*90
    counts[12] = counts[12]*15
    counts[13] = counts[13]*40
    counts[14] = counts[14]*10
    counts[15] = np.floor(counts[15]/5)*200 + counts[15] % 5 * 50
    counts[16] = np.floor(counts[16]/3)*80 + counts[16] % 3 * 30
    counts[17] = counts[17]*50
    counts[18] = counts[18]*20
    counts[19] = counts[19]*20
    counts[20] = np.floor(counts[20]/4)*120 + counts[20] % 4 *40
    counts[21] = np.floor(counts[21]/3)*130 + np.floor((counts[21]%3)/2)*90+ ((counts[21]%3) % 2) * 50
    counts[22] = counts[22]*20
    counts[23] = counts[23]*17
    counts[24] = counts[24]*20
    counts[25] = counts[25]*21


    total = np.sum(counts)

    return total



