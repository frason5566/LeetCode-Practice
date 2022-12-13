def R(rings):
    
    rods = [[]for _ in range(10)]
    for i in range(0, len(rings), 2):
        ring = rings[i]
        rod_idx = ord(rings[i+1]) - ord('0')
        if ring not in rods[rod_idx]:
            rods[rod_idx].append(ring)
    # print(rods)
    res = 0 
    for i in range(10):
        if len(rods[i]) == 3:
            res += 1
    return res

def main():
    R('B0B6G0R6R0R6G9G1R1B1')

main()