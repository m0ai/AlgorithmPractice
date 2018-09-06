# 사슬 (Concatenate)

두개 이상의 arrays는 튜플은 concatenate 함수를 이용하여 하나의 튜플로 매듭(결합)지을 수 있습니다.


```python
import numpy
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
```

만약 array가 이차원 배열일 경우, 여러배열이 연결된 축을 지정할 수 있습니다.
기본적으로 일차원 배열을 따릅니다.


```python
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]    
```

## Task
여러분들은 크기가 N * P 와 M * P인 두개의 배열을 가집니다.
N과 M은 행, P는 열을 나타냅니다). 여러분은 asix 0로 배열을 연결하는 것 입니다.

## Input Format

 첫번째 라인에선 N, M, P 정수 입력 받으며 space로 구분된 값을 입력 받습니다.
두번째에선 N줄에선 P열의 space로 값이 구분된 값을 입력 받습니다.

## Sample Input
```
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
```
## Sample Output
```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
```
