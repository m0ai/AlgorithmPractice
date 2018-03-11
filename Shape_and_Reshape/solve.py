import numpy

user_input  = raw_input()
array_data = numpy.array(map(int, user_input.split()))
print numpy.reshape(array_data, (3,3))
