def O(s):
    """
    :type s: str
    :rtype: int
    """
    Lc=[]
    maxL = 0
    for i in range(len(s)): 
        if s[i] not in Lc:
            Lc.append(s[i])
            # print("Lc Append", s[i])
            # maxL = len(Lc)
        else:    
            maxL = len(Lc) if len(Lc)>maxL else maxL
            index = Lc.index(s[i])
            Lc = Lc[index+1:]
            Lc.append(s[i])
            # print("Lc = ", Lc)
        maxL = len(Lc) if len(Lc)>maxL else maxL    
    return maxL
            
def main():
    Str1 = "abcabccba"
    Str2 = "dvdf"
    Str3 = "abcccccdba"
    Str4 = "pwwkew"
    Str5 = "aab"
    print(O(Str1))
    print(O(Str2))
    print(O(Str3))
    print(O(Str4))
    print(O(Str5))


main()