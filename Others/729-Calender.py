# class MyCalendar:

#     def __init__(self):
#         self.booking=[]
        

#     def book(self, start: int, end: int) -> bool:
#         res = True
#         for i in range(len(self.booking)):
#             if res:
#                 if (start < self.booking[i][0] and end <= self.booking[i][0]) or (start >= self.booking[i][1]):
#                     res = True
#                 else:
#                     res = False

#         if res:
#             self.booking.append([start,end])
#         self.booking.sort(key = lambda x: x[0])
#         print(self.booking)

#         return res
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root == None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

def main():
    obj = MyCalendar()
    print(obj.book(47,50))
    print(obj.book(33,41))
    print(obj.book(39,45))
    print(obj.book(33,42))
    print(obj.book(25,32))
    print(obj.book(26,35))
    print(obj.book(19,25))
    print(obj.book(3,8))
    print(obj.book(8,13))
    print(obj.book(18,27))


main()