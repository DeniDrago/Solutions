class FibonacciIterator:
    def __init__(self, number):
        self.number = number
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.number:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.a


fibonacci = FibonacciIterator(20)
for num in fibonacci:
    print(num)
