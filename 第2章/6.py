a = (22, 1, 42, 10)
b = (20, 0, 36, 8)


def euclidean_distance(x, y):
    '''计算这两个对象之间的欧几里得距离'''
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) ** 2
    return sum ** 0.5


def manhattan_distance(x, y):
    '''计算这两个对象之间的曼哈顿距离'''
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i] - y[i])
    return sum


def minkowski_distance(x, y, q):
    '''使用 q = 3，计算这两个对象之间的闵可夫斯基距离'''
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i] - y[i]) ** q
    return sum ** (1 / q)


def upper_bound_distance(x, y):
    '''计算这两个对象之间的上确界距离'''
    max = 0
    for i in range(len(x)):
        if abs(x[i] - y[i]) > max:
            max = abs(x[i] - y[i])
    return max


print(euclidean_distance(a, b))
print(manhattan_distance(a, b))
print(minkowski_distance(a, b, 3))
print(upper_bound_distance(a, b))
