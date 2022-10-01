import rbtree

class intervals:
    def __init__(self, input):
        self.input = input
        self.rbtree = rbtree.RedBlackTree()

    def insertSuccess(self, interval, position, prime):
        self.rbtree.insert(interval)
        search = self.rbtree.search(interval)
        predecessor = self.rbtree.predecessor(search)
        numberOfDigits = len(str(prime))
        if interval[0] == 0:
            self.input.print(f'Prime: {prime}, Position: {position}')
        elif predecessor is not None:
            if predecessor.item[1]-numberOfDigits+1 == interval[0] and predecessor.item[0] == 0:
                self.input.print(f'Prime: {prime}, Position: {position}')

    def insertFail(self, interval):
        pass


class successInterval(intervals):
    def __init__(self, interval, prime, position, input):
        super().__init__(input)
        self.interval = interval
        self.prime = prime
        self.position = position

    def isSuccess(self):
        return True

class failInterval(intervals):
    def __init__(self, interval, input):
        super().__init__(input)
        self.interval = interval

    def isSuccess(self):
        return False