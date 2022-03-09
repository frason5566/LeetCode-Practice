def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    L=[]
    Lc=[]
    flag = 0 
    for i in range (len(s)):
        Lc.append(s[i])
        for j in range (i + 1, len(s)):
            for item in Lc:
                if s[j]==item:
                    flag = 1
            if flag == 0:
                Lc.append(s[j])
        if len(Lc)>len(L):
            L = Lc
        Lc = []
            
    return len(L)
            