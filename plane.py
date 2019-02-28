import numpy as np
from function import *
from numpy import dot # cкалярное произведение
import matplotlib.pyplot as plt

def test():
    r0 = [3,3]
    e = norm_v([1,-1])
    n = norm_v([1,0])
    rp0 = [1,6]
    return r0,e,rp0,n

def get_reflection(e, n):
    return sub(e, mult(n, 2 * dot(e, n)))


def get_refraction(e, n, n1, n2):
    sq = np.sqrt((1-n1**2/n2**2 * (1-(dot(e,n))**2)))
    t = n2*sq
    t2 = n1*dot(e,n)
    t3 = t2 - t
    t4 = mult(n,t3)
    t5 = mult(e,n1)
    t6 = sub(t5,t4)
    mult(t6, 1/n2)
    return norm_v(t6)

def plane():

    r0,e,rp0,n = test()

    t = (dot(n,sub(r0,rp0)))/(dot(n,e))
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
    refraction_e = mult(get_refraction(e, n, 1, 1), t)
    refraction_a = (cross_point[0] + refraction_e[0], cross_point[1] + refraction_e[1])
    plt.plot([cross_point[0], refraction_a[0]], [cross_point[1], refraction_a[1]])

    plt.legend(("Плоскость", "Падающий луч","Отраженный луч", "Преломленный "))

    plt.grid()
    plt.show()


plane()