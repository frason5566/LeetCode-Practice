def M(words):
    if len(words) == 1: return 1
    ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res = []
    for word in words:
        temp = ''
        for l in word:
            temp += ref[ord(l)- ord('a')]
        res.append(temp)
    return len(set(res))

def main():
    W = ["gin","zen","gig","msg"]
    print(M(W))


main()
    