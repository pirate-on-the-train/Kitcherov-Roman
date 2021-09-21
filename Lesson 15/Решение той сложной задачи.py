import math

def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 += math.trunc(aug + p0 * (percent / 100))
        count += 1
    return count