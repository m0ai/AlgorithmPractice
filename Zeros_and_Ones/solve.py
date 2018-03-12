import numpy

user_input = tuple(map(int, raw_input().split()))

print numpy.zeros(user_input, dtype=numpy.int)
print numpy.ones(user_input, dtype=numpy.int)
