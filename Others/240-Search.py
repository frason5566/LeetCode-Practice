def S(matrix, target):
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False
def SS(matrix, target):
    x,y = len(matrix[0])-1, 0
    while x>=0 and y < len(matrix):
        if matrix[y][x] == target:
            return True
        elif matrix[y][x] < target:
            y+=1
        elif matrix[y][x] > target:
            x-=1

    return False


def main():
    M = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(SS(M,5))
    print(SS(M,30))
    print(SS(M,20))
main()