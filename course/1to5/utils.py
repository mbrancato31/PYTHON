

def findMax(num):
    maxi = num[0]

    for n in num:
        if n > maxi:
            maxi = n

    return maxi