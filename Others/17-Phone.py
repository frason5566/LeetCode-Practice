def P(digits):
    ref = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    num = []
    res = []
    for i in range(len(digits)):
        if digits[i] == '2':
            num=[0] + num
        elif digits[i] == '3':
            num=[1] + num
        elif digits[i] == '4':
            num=[2] + num
        elif digits[i] == '5':
            num=[3] + num
        elif digits[i] == '6':
            num=[4] + num
        elif digits[i] == '7':
            num=[5] + num
        elif digits[i] == '8':
            num=[6] + num
        elif digits[i] == '9':
            num=[7] + num
    
    for item in num:
        if len(res) == 0:
            for letter in ref[item]:
                res.append(letter)
        else:
            temp=[]
            for letter in ref[item]:
                for word in res:
                    temp.append(letter+word)
            res = temp
    # print(res)
    return res


def main():
    D = '23'
    print(P(D))
    D = '5472'
    print(P(D))

main()