# a = [1,2,3]
#
# a_iter = iter(a)
# print(next(a_iter))
# for i in a:
#     print(i)
# print()
# for i in a:
#     print(i)


# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         #print("In __iter__")
#         return self
#
#     def __next__(self):
#         #print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
# sq = SquareIterator(2, 5)
# # sq_iter = iter(sq)
# # print(next(sq_iter))
# # print(next(sq_iter))
# # print(next(sq_iter))
# # print(next(sq_iter))
#
# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

#####################################################3

# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         #print("In __iter__")
#         return SquareIterator(self.start, self.stop)
#
#     def __next__(self):
#         #print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
#
# sq = SquareIterator(2, 5)
#
# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

#####################################################3

# class SquareIteratorLogic:
#
#     def __init__(self, start, stop):
#         self.current = start
#         self.stop = stop
#
#     def __next__(self):
#         #print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
#
# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         #print("In __iter__")
#         return SquareIteratorLogic(self.start, self.stop)
#
#
# sq = SquareIterator(2, 5)
#
# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

#####################################################3
class SquareIterator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        #self.current = start

    def __iter__(self):
        #print("In __iter__")
        self.current = self.start
        return self

    def __next__(self):
        #print("In __next__")
        if self.current < self.stop:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration


sq = SquareIterator(2, 5)

# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

sq_iter1 = iter(sq)


print(f"1: {next(sq_iter1)}")

sq_iter2 = iter(sq)
print(f"1: {next(sq_iter1)}")

print(f"2: {next(sq_iter1)}")