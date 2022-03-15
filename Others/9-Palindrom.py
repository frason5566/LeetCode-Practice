def P(n):
    if n < 0: return False
    tempn = n
    temp = 0
    while tempn != 0:
        temp = temp * 10 + tempn % 10
        tempn = tempn // 10
    return True if temp == n else False
    


def main():
   N = 121
   print(P(N))
   N = 12
   print(P(N))
   N = 10
   print(P(N))
   N = -121
   print(P(N))


main()