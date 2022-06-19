def S(products, searchWord):
    res = []
    F = [True] * len(products)
    products.sort()
    print(products)
    
    for i in range(len(searchWord)):
        temp = []
        for word in products:
            if len(word) > i:
                if word[i] == searchWord[i] and len(temp) < 3 and F[products.index(word)] == True:
                    print(".")
                    temp.append(word)
                elif word[i] != searchWord[i]:
                    F[products.index(word)] = False
        res.append(temp)
    return res


def main():
    Ws = ["mobile","mouse","moneypot","monitor","mousepad"]
    print(Ws)
    w = "mouse"
    print(S(Ws,w))
    Ws = ["code","codephone","coddle","coddles","codes"]
    w = "coddle"
    print(S(Ws,w))
    # P = [1]
    # print(P[:3])

main()