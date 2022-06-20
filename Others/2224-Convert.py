def C(current, correct):
    ch = int(current[:2])
    cm = int(current[3:])
    th = int(correct[:2])
    tm = int(correct[3:])
    cnt = 0
    while cm != tm:
        if tm < cm:
            tm += 60
            th -= 1
        dif = tm - cm
        if dif >= 15:
            tm -= 15
        elif dif < 15 and dif >= 5:
            tm -= 5
        elif dif <5 and dif >= 1:
            tm -= 1
        cnt += 1

    while th < ch:
        th += 12
    cnt += th - ch
    
    return cnt


def main():
    print(C("02:30","04:35"))
    print(C("11:35","14:45"))

main()