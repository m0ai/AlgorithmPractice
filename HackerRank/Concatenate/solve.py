import numpy


def array_input(line):
    return [map(int, raw_input().split()) for _ in range(line)]


N, M, P = map(int, raw_input().split())

first_array = numpy.array(array_input(N))
second_array = numpy.array(array_input(M))

print numpy.concatenate((first_array, second_array), axis=0)
