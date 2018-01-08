# wrong
def sum(a, b):
    a = a + b


# correct
def sum1(a, b):
    a = a + b
    return a


print sum1(1, 2)
