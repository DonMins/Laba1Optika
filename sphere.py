import numpy as np
from numpy import dot # cкалярное произведение
from function import *
import matplotlib.pyplot as plt


def intersection_with_sphere(r0, R, p0, e):
    temp = (dot(sub(r0, p0), e) ** 2) - (dot(sub(r0, p0), sub(r0, p0)) - R ** 2)
    if temp < 0:
        print('Луч не пересекает сферу')
    else:
        t1 = abs((dot(sub(r0, p0), e)) - np.sqrt(temp))
        t2 = abs((dot(sub(r0, p0), e)) + np.sqrt(temp))
        if p0[0]-R/2<r0[0]<p0[0]+R/2:
            return max(t1,t2)
        else:
            return min(t1,t2)


def normal(r0, e, p0, t):
    temp = sub(sum(r0, mult(e, t)), p0)
    n = mult(temp, 1 / np.sqrt(dot(temp, temp)))
    n = norm_v(n)

    return n


def plot_sphere(p0, R):
    i = np.linspace(0, 2 * np.pi, 100)
    plt.plot(R * np.cos(i) + p0[0], R * np.sin(i) + p0[1])




def reflection_from_sphere(e, n):
    e_refl = sub(e, mult(n, 2 * dot(e, n)))
    e_refl = norm_v(e_refl)
    return e_refl


def refraction_after_sphere(n_refr, e, n):
    e_refr = sub(mult(e, n_refr[0]), mult(mult(n, sign(dot(e, n))), n_refr[0] * abs(dot(e, n)) -
                                          n_refr[1] * np.sqrt(
        1 - (n_refr[0] / n_refr[1]) ** 2 * (1 - (dot(e, n) ** 2)))))
    e_refr = mult(e_refr, 1 / n_refr[1])
    e_refr = norm_v(e_refr)
    return e_refr


def plot_ray(r0, e, t, name):
    j = np.linspace(0, t, 100)
    x = r0[0] + e[0] * j
    y = r0[1] + e[1] * j
    plt.plot(x, y, label=name)
