# Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей
# составленных из элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
from typing import Tuple, Iterable, List


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    sequence_list = list(sequences)
    func_result = []
    minimal_len = min(map(len, sequences))
    maximal_len = max(map(len, sequences))
    if full:
        for argument in sequence_list:
            argument = list(argument.append(default) for _ in range(maximal_len - len(argument))
                            if len(argument) < maximal_len)
        for i in range(maximal_len):
            element = []
            for arg in sequence_list:
                element.append(arg[i])
            func_result.append(tuple(element))
    else:
        for i in range(minimal_len):
            element = []
            for arg in sequence_list:
                element.append(arg[i])
            func_result.append(tuple(element))
    return func_result


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
seq3 = [11, 12, 13, 14, 15, 16]
seq4 = [15, 16]
assert (custom_zip(seq1, seq2)) == [(1, 9), (2, 8), (3, 7)]
assert (custom_zip(seq1, seq2, full=True, default="Q")) == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

print(custom_zip(seq1, seq2, seq3, seq4, full=True, default="RRR"))
