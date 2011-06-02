found = False
count = 0
factor = 2520 * 11 * 13 * 17 * 19


def valid(num):
    for i in range(2,21):
        if (test % i) != 0:
            return False
    return True


while not found:
    count += 1
    test = count * factor
    if valid(test):
        found = True

print test
