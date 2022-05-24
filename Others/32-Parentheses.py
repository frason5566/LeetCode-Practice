# def L(s):
#     res = 0
    
#     l,r = 0,0
#     s2 = ''
#     for c in s:
#         if c == '(':
#             l += 1
#         else:
#             r += 1
#         if l == r:
#             res = max(res,r*2)
#         elif r >= l:
#             r,l = 0,0
#         s2 = c+s2
#     # print(s2)
#     r,l = 0,0
#     for c in s2 :
#         if c == ')':
#             r += 1
#         else:
#             l += 1
#         if l == r:
#             res = max(res,l*2)
#         elif l >= r:
#             r,l = 0,0

#     return res

def L(s):
    res = 0
    len(s)
    l,r = 0,0
    for i in range(len(s)):
        if s[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            res = max(res,r*2)
        elif r >= l:
            r,l = 0,0
    r,l = 0,0
    for i in range(len(s)-1,-1,-1) :
        if s[i] == ')':
            r += 1
        else:
            l += 1
        if l == r:
            res = max(res,l*2)
        elif l >= r:
            r,l = 0,0

    return res


def main():

    S="(()"
    print(L(S))
    S=")()())"
    print(L(S))
    S="(())()"
    print(L(S))

main()