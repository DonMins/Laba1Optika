import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Intersection:
    def __init__(self, dots=None, t=0):
        if dots is None:
            dots = []
        self.dots = dots
        self.t = t


def normal(abc, intersept, ellips):
    n = []
    for i in range(len(abc)):
        n.append(2*(intersept[i] - ellips[i])/abc[i]**2)
    return n


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


def scal_mult(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    return res


def k_mult(v, k):
    res = []
    for i in range(len(v)):
        res.append(v[i] * k)
    return res


def calc_t(r0, e, rp0, n):
    return np.dot(sub(rp0, r0), n) / np.dot(e, n)


def calc_crossing_point(r0, e, t):
    return sum(r0, k_mult(e, t))


def get_v():
    v = str(input()).split(' ')
    result = []
    for e in v:
        result.append(float(e))
    return result


def get_len(v):
    result = 0
    for i in range(len(v)):
        result += v[i] ** 2
    return np.sqrt(result)


def norm_v(v):
    l = get_len(v)
    for i in range(len(v)):
        v[i] = v[i] / l
    return v


def mult_abc(abc, v):
    res = [v[0] * abc[1] * abc[2], v[1] * abc[0] * abc[2], v[2] * abc[0] * abc[1]]
    return res


def get_reflection(e, n):
    return sub(e, k_mult(n, 2 * scal_mult(e, n)))


def get_refraction(e, n, n1, n2):
    new_e = sub(k_mult(e, n1), k_mult(n, scal_mult(e, n)*n1*(1-np.sqrt(((n2**2)-(n1**2))/((scal_mult(e, n)**2)*(n1**2)) + 1))))
    return k_mult(new_e, 1/n2)

def plane_intersection(r0, e, rp0, n):
    parallel_flag = False
    contains_flag = False
    if np.dot(e, n) == 0:
        parallel_flag = True
    if np.dot(sub(rp0, r0), n) == 0:
        contains_flag = True
    if parallel_flag and contains_flag:
        print("Прямая лежит в плоскости")
    if parallel_flag and not contains_flag:
        print("Прямая параллельна плоскости")
    if not parallel_flag:
        t = calc_t(r0, e, rp0, n)
        print("Длина отрезка" + str(t))
        print("Точка пересечения" + str(calc_crossing_point(r0, e, t)))
        return t, calc_crossing_point(r0, e, t)


def plane():
    print("Enter r0:")
    r0 = get_v()
    print("Enter e:")
    e = norm_v(get_v())
    print("Enter rp0:")
    rp0 = get_v()
    print("Enter n:")
    n = norm_v(get_v())
    if plane_intersection(r0, e, rp0, n) is not None:
        t, cross_point = plane_intersection(r0, e, rp0, n)

        reflection_e = k_mult(get_reflection(e, n), t)
        refraction_e = k_mult(get_refraction(e, n, 1, 2), t)

        # Отрисовать плоскость
        a = (cross_point[0] - n[1], cross_point[1] + n[0])
        b = (cross_point[0] + n[1], cross_point[1] - n[0])
        plt.plot([a[0], b[0]], [a[1], b[1]])
        # Отрисовать прямую
        plt.plot([r0[0], cross_point[0]], [r0[1], cross_point[1]])
        # Отражённый луч
        reflection_a = (cross_point[0] + reflection_e[0], cross_point[1] + reflection_e[1])
        plt.plot([cross_point[0], reflection_a[0]], [cross_point[1], reflection_a[1]])
        # Преломлённый луч
        refraction_a = (cross_point[0] + refraction_e[0], cross_point[1] + refraction_e[1])
        plt.plot([cross_point[0], refraction_a[0]], [cross_point[1], refraction_a[1]])

        plt.axis([0, 10, 0, 10])
        plt.grid(True)
        plt.show()


plane()

