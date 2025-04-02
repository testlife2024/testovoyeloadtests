import sys


def circular_array(a, b):
    c_array = list(range(1, a + 1))  # создали массив из входных элементов
    ind = 0
    path = []
    while True:  # создание пути ( цикл работает, пока первый элемент не будет равен последнему )
        path.append(c_array[ind])
        ind = ((ind + b) % a) - 1
        if ind == 0:
            break
    return path


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
result = circular_array(n, m)
print(result)
sys.exit(0)
