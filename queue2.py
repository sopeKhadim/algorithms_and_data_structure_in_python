class Queue:

    def __init__(self, size):
        self.N = 0
        self.head = 0
        self.tail = 0
        self.array = [0] * size
        self.size = size

    def enqueue(self, elem):
        self.array[self.tail] = elem
        if self.tail == self.size - 1:
            self.tail = 1
        else:
            self.tail += 1
        self.N += 1

    def dequeue(self):
        x = self.array[self.head]
        if self.head == self.size - 1:
            self.head = 1
        else:
            self.head += 1
        self.N -= 1
        return x

    def is_empty(self):
        return self.N == 0

    def printQueue(self):
        head = self.head
        tail = self.tail
        print("--Printing the Queue--")
        while head != tail - 1:
            print(self.array[head], "->", end=' ')
            head = (head + 1) % self.size
        print(self.array[head], end='\n')


if __name__ == '__main__':
    myqueue = Queue(10)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    myqueue.enqueue(6)
    myqueue.enqueue(6)
    myqueue.printQueue()
    print("Removing FIFO", myqueue.dequeue())
    print("Removing FIFO", myqueue.dequeue())
    myqueue.printQueue()
