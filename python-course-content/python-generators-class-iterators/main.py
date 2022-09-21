class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


gen = FirstHundredGenerator()

print(next(gen))
print(next(gen))
print(next(gen))

# Iterator: not generate new numbers, keep track of i value
# return number in a list not generate new numbers
# class FirstFiveIterator:
#     def __init__(self):
#         self.numbers = [1, 2, 3, 4, 5]
#         self.i = 0

#     def __next__(self):
#         if self.i < len(self.numbers):
#             current = self.numbers[self.i]
#             self.i += 1
#             return current
#         else:
#             raise StopIteration()


# iterator = FirstFiveIterator()
# print(next(iterator))
# print(next(iterator))

# for i in gen:
#     print(i, end=' ')

# sum(gen)
# list(gen)
