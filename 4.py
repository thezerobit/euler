largest = 1
fa = 0
fb = 0

def is_palindromic(num):
    teststr = str(num)
    length = len(teststr)
    ntests = length / 2
    for i in range(ntests):
        if teststr[i] != teststr[length - i - 1]:
            return False
    return True

for x in range(100,1000):
    for y in range(x, 1000): 
        product = x * y
        if is_palindromic(product):
            if product > largest:
                largest = product 
                fa = x
                fb = y

print "%d * %d = %d"%(fa, fb, largest)
