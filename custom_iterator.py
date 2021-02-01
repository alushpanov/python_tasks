class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return self.data[self.index]


custom_iter = CustomIterator('abcde')
custom_iter = CustomIterator([1, 2, 3, 4, 5, 6])
# custom_iter = CustomIterator([])
for elem in custom_iter:
    print(elem)