def S(words1, words2):
    def count(word):
        a = [0] * 26
        for l in word:
            a[ord(l)- ord('a')] += 1
        return a
    bmax = [0]*26
    for word in words2:
        for i, c in enumerate(count(word)):
            bmax[i] = max(bmax[i], c)
    ans=[]
    for word in words1:
        if all(x>=y for x,y in zip(count(word), bmax)):
            ans.append(word)

    return ans

def main():
    W1 = ["amazon","apple","facebook","google","leetcode"]
    W2 = ["e","o"]
    print(S(W1,W2))
    W1 = ["amazon","apple","facebook","google","leetcode"]
    W2 = ["le","e"]
    print(S(W1,W2))


main()