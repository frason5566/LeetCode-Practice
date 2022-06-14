def F(names):
    K = [0] * len(names)
    s = set()
    for i in range(names):
        if names[i] not in s:
            s.add(names[i])
        else:
            while names[i] in set():
                K[names.index(names[i])]+=1
                names[i] = names[i] + '(' + K[]


        



    return

def main():
    N = ['gta','gta','gta(1)']
    print(F(N))

main()