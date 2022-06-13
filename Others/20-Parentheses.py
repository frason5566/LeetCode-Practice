def P(s):
    temp = []
    for l in s:
        if l == "(" or l == "[" or l == "{":
            temp.append(l)
        elif len(temp) == 0:
            return False
        elif l == ')':
            c = temp.pop()
            if c != '(':
                return False
        elif l == ']':
            c = temp.pop()
            if c != '[':
                return False
        elif l == '}':
            c = temp.pop()
            if c != '{':
                return False
    if len(temp) != 0:
        return False

    return True

def main():
    s = "(]"
    print(P(s))
    s = "({}[])"
    print(P(s))
    s = "]"
    print(P(s))

main()