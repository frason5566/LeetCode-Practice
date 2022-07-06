from math import sqrt
def fib(n):
    a = 0 
    b = 1
    for i in range(n): 
        a, b = b, a + b
    return a

def ff(n):
    alpha = (1 + sqrt(5))/2
    beta = (1-sqrt(5))/2
    return int(5**(-1/2) * (alpha**n - beta**n))
def main():

    print(ff(8))
    

main()