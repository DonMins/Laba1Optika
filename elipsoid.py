import numpy as np
from numpy import dot # cкалярное произведение
from function import *
import matplotlib.pyplot as plt
import  numpy as np

# def normal(r0, e, p0, t):
#     temp = sub(sum(r0, mult(e,t)), p0)
#     n = mult(temp,1 / np.sqrt(dot(temp, temp)))
#     n = norm_v(n)
#     return n

def derivative(x0,y0,a,b):
    return -(x0 * (b ** 2)) / (y0 * (a ** 2))

def normal(x0,y0,a,b):
    a =derivative(x0,y0,a,b)
    a = np.arctan(a)
    return np.array([np.cos(a), np.sin(a)])



def refraction_after_ellipsoid(n_refr, e, n):
    e_refr = sub(mult(e,n_refr[0]), mult(mult(n,sign(dot(e, n))),n_refr[0] * abs(dot(e, n)) - n_refr[1] * np.sqrt(
        1 - pow(n_refr[0] / n_refr[1], 2) * (1 - pow(dot(e, n), 2)))
                                                 ))
    e_refr = mult( e_refr,1 / n_refr[1])
    e_refr = norm_v(e_refr)
    return e_refr


def reflection_from_ellipsoid(e, n):
    e_refl = sub(e, mult(n,2 * dot(e, n)))
    e_refl = norm_v(e_refl)
    return e_refl

def intersection_with_ellipsoid(r0, e, p0, a_el, b_el):
    temp1 = [b_el * e[0], a_el * e[1]]
    temp2 = [b_el * (r0[0] - p0[0]), a_el * (r0[1] - p0[1])]
    a = dot(temp1, temp1)
    b = 2 * dot(temp1, temp2)
    c = dot(temp2, temp2) - pow(a_el*b_el, 2)
    D = b * b - 4 * a * c
    if D < 0:
        print('Луч не пересекает эллипс')
    else:
        t1 = (- b - np.sqrt(D)) / (2 * a)
        t2 = (- b + np.sqrt(D)) / (2 * a)
        if t1 < 0:
            if t2 < 0:
                print('Луч не пересекает эллипс')
            else:
                return t2
        elif t2 < 0:
            return t1
        else:
            return min(t1, t2)

def plot_ellipsoid(p0, a, b):
    i = np.linspace(0, 2 * np.pi, 100)
    plt.plot(a * np.cos(i) + p0[0], b * np.sin(i) + p0[1])

def plot_ray(r0, e, t, name):
    j = np.linspace(0, t, 100)
    x = r0[0] + e[0] * j
    y = r0[1] + e[1] * j
    plt.plot(x, y, label=name)