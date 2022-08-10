class HashTable:
    hashT = [[], ]
    N = 0

    def __init__(self, N):
        self.N = N
        self.hashT = [[], ] * N

    @staticmethod
    def check_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        return True

    def get_prime(self, n):
        if n % 2 == 0:
            n = n + 1
        while not self.check_prime(n):
            n += 2

        return n

    def hashFunction(self, key):
        capacity = self.getPrime(10)
        return key % capacity

    def insertData(self, key, data):
        index = self.hashFunction(key)
        self.hashT[index] = [key, data]

    def removeData(self, key):
        index = self.hashFunction(key)
        self.hashT[index] = 0

    def __str__(self):
        return self.hashT.__str__()

    def __repr__(self):
        return self.hashT.__repr__()


if __name__ == '__main__':
    hTable = HashTable(10)
    hTable.insertData(123, "apple")
    hTable.insertData(432, "mango")
    hTable.insertData(213, "banana")
    hTable.insertData(654, "guava")
    print("Print Hash Table :")
    print(hTable)

    print("Remove element (key = 123, apple)")
    hTable.removeData(123)

    print("Print Hash table after deletion")
    print(hTable)
