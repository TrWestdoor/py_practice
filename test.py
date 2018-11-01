def findMinAndMax(L):
    if L == []:
        return (None, None)
    Lmin = min(L)
    Lmax = max(L)
    return(Lmin, Lmax)

if findMinAndMax([]) != (None, None):
    print('Error!')
elif findMinAndMax([7])!= (7,7):
    print('Error!')
elif findMinAndMax([7,1]) != (1,7):
    print('Error!')
elif findMinAndMax([7,1,3,9,5]) != (1, 9):
    print('Error!')
else:
    print('Successful!')

