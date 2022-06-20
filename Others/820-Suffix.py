def S(words):
    words.sort(key=len,reverse=True) # sorting based on the length of words
    print(words)
    ans=''
    for x in words: # iterating over each words
        if x+'#' not in ans:   # if that particular word is not present in our reference string then we are adding it to our answer
            ans+=x+'#'
    return len(ans)

def main():
    W = ["time","me","bell"]
    print(S(W))


main()
