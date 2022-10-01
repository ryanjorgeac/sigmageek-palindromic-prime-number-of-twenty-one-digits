import rbtree

class intervals:
    def __init__(self, input):
        self.input = input
        self.rbtree = rbtree.RedBlackTree()

    def insertSuccess(self, interval, position, prime):
        self.rbtree.insert(interval)
        item = self.rbtree.predecessor(self.rbtree.search(interval)).item
        numberOfDigits = len(str(prime))
        if interval[0] == 0 or item[1]-numberOfDigits+1 == interval[0]:
            self.input.print(f'Prime: {prime}, Position: {position}')

    def insertFail(self, interval):
        pass