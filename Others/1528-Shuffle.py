def S(s, indices):
    temp = [' 'for _ in range(len(s))]
    for i, c in enumerate(s):
        temp[indices[i]] = c
    return ''.join(temp)

def main():
    print(S('codeleet', [4,5,6,7,0,2,1,3]))
    
main()