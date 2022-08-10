class Deque:

    def __init__(self, size):
        self.N = 0
        self.head = 0
        self.tail = size - 1
        self.array = [0] * size
        self.size = size

    def add_first(self, item):
        self.array[self.head] = item
        self.N += 1
        self.head = (self.head + 1) % self.size

    def add_last(self, item):
        self.array[self.tail] = item
        self.N += 1
        self.tail = (self.tail - 1) % self.size

    def remove_first(self):
        self.N -= 1
        self.head = (self.head - 1) % self.size
        v = self.array[self.head]
        return v

    def remove_last(self):
        self.N -= 1
        self.tail = (self.tail + 1) % self.size
        v = self.array[self.tail]
        return v

    def print_all(self):

        head = (self.head - 1) % self.size
        tail = (self.tail + 1) % self.size
        print("--Printing the Dequeue--")
        while head != tail:
            print(self.array[head], "->", end=' ')
            head = (head - 1) % self.size
        print(self.array[head], end='\n')


if __name__ == '__main__':
    myqueue = Deque(20)
    myqueue.add_first(2)
    myqueue.add_first(3)
    myqueue.add_first(4)
    myqueue.add_last(5)
    myqueue.add_last(6)
    myqueue.add_last(1)
    myqueue.add_last(9)
    myqueue.print_all()
    print(myqueue.remove_last())
    print(myqueue.remove_first())
    myqueue.print_all()
    myqueue.add_last(7)
    myqueue.print_all()
    print(myqueue.remove_first())
    myqueue.print_all()

