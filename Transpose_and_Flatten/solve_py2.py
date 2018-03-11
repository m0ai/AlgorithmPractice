import numpy
import itertools

row, col= map(int, raw_input().split())#"2 2\n1 2\n3 4"
data = map(int, list(itertools.chain.from_iterable([raw_input().split() for _ in range(row)])))
elements = numpy.array(data)

reshaped_array = numpy.reshape(elements, (row, col))

print(numpy.transpose(reshaped_array))
print(reshaped_array.flatten())
