import numpy as np

#  модуль вектора
def get_len(v):
    result = 0
    for i in range(len(v)):
        result += v[i] ** 2
    return np.sqrt(result)

# нормировка
def norm_v(v):
    l = get_len(v)
    for i in range(len(v)):
        v[i] = v[i] / l
    return v

# ввод значений
def get_v():
    v = str(input()).split(' ')
    result = []
    for e in v:
        result.append(float(e))
    return result

def sub(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] - b[i])
    return res

def sum(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return res

def mult(v, k):
    res = []
    for i in range(len(v)):
        res.append(v[i] * k)
    return res

def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1