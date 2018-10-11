#############
#First Method
#############
from math import sqrt
gamma = (3 - sqrt(5))/2
f = lambda x: x ** 4 + x**2 -2*x
def goldenSectionSearchRecursive(f, a, c, b, tol):
    if abs(a - b) < tol:
        return (a + b) / 2
    d = c + gamma * (b - c)
    if f(d) < f(c):
        return goldenSectionSearch(f, c, d, b, tol)
    else:
        return goldenSectionSearch(f, d, c, a, tol)
goldenSectionSearchRecursive(f, -4,gamma, 5, 1e-5)

##############
#Second Method
##############
from math import sqrt
gamma = (math.sqrt(5) + 1) / 2
f = lambda x: x ** 4 + x**2 -2*x

def goldenSectionSearchIterative(f, a, b, tol=1e-5):
    c = b - (b - a) / gamma
    d = a + (b - a) / gamma
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gamma
        d = a + (b - a) / gamma
    return (b + a) / 2
goldenSectionSearchIterative(f,-4,5)

#############
#Third Method
#############
from math import sqrt
gamma = (3 - sqrt(5))/2
f = lambda x: x ** 4 + x**2 -2*x

def goldenSectionSearchIterativeSecond(f, a, b, tol=1e-5):
    c = b - (b - a) * gamma
    d = a + (b - a) * gamma
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) * gamma
        d = a + (b - a) * gamma
    return (b + a) / 2
goldenSectionSearchIterativeSecond(f,-4,5)
