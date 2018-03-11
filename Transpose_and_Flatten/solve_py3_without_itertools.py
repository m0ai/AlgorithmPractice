import numpy

def merge(*iters):
    for it in iters:
        yield from it

row, col = map(int, input().split())#"2 2\n1 2\n3 4"
data = map(int, sum(list(merge([input().split() for _ in range(row)])), []))
elements = numpy.array(list(data))
reshaped_array = numpy.reshape(elements, (row, col))

print(numpy.transpose(reshaped_array))
print(reshaped_array.flatten())
