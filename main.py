import numpy as np
import matplotlib.pyplot as plt
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

def scal_mult(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    return res

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
def test():
    r0 = [3,3]
    e = norm_v([1,-1])
    n = norm_v([1,-0.5])
    rp0 = [1,6]
    return r0,e,rp0,n

def get_reflection(e, n):
    return sub(e, mult(n, 2 * scal_mult(e, n)))



def get_refraction(e, n, n1, n2):
    sq = np.sqrt((1-n1**2/n2**2 * (1-(scal_mult(e,n))**2)))

    t = n2*sq

    t2 = n1*scal_mult(e,n)

    t3 = t2 - t

    t4 = mult(n,t3)
    t5 = mult(e,n1)
    t6 = sub(t5,t4)
    mult(t6, 1/n2)

    return norm_v(t6)

def plane():
    # print("Enter r0:")
    # r0 = get_v()
    # print("Enter e:")
    # e = norm_v(get_v())
    # print("Enter rp0:")
    # rp0 = get_v()
    # print("Enter n:")
    # n = norm_v(get_v())

    r0,e,rp0,n = test()

    t = (scal_mult(n,sub(r0,rp0)))/(scal_mult(n,e))
    print("Длина луча ", t)

    cross_point = sum(rp0, (mult(e,t)))
    print("Точка пересечения " , cross_point)
    a = (cross_point[0] - n[1], cross_point[1] + n[0])
    b = (cross_point[0] + n[1], cross_point[1] - n[0])

    # Падающий луч
    plt.plot([a[0], b[0]], [a[1], b[1]])
    plt.plot([rp0[0], cross_point[0]], [rp0[1], cross_point[1]])

    # Отражённый луч
    reflection_e = mult(get_reflection(e, n), t)
    reflection_a = (cross_point[0] + reflection_e[0], cross_point[1] + reflection_e[1])
    plt.plot([cross_point[0], reflection_a[0]], [cross_point[1], reflection_a[1]])

    # Преломлённый луч
    refraction_e = mult(get_refraction(e, n, 1, 4), t)
    refraction_a = (cross_point[0] + refraction_e[0], cross_point[1] + refraction_e[1])
    plt.plot([cross_point[0], refraction_a[0]], [cross_point[1], refraction_a[1]])

    plt.legend(("Плоскость", "Падающий луч","Отраженный луч", "Преломленный "))

    plt.grid()
    plt.show()


plane()