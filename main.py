import sphere
import matplotlib.pyplot as plt
from elipsoid import *
import math
import numpy as np

def test():
    p0 = [0, 0]  # Введите радиус-вектор центра сферы
    R = 4  # Радиус сферы
    r0 = [-5, 2]  # Введите радиус-вектор начала луча
    e = sphere.norm_v([1, -1])  # вектор направления луча
    n_r = [1, 2]  # кф преломления
    return p0, R, r0, e, n_r

def testElips():

    r0 = [1, 1]  # Введите радиус-вектор начала луча
    e = norm_v([1, -1])  # вектор направления луча
    n_r = [1, 2]  # кф преломления
    a = 3
    b = 2
    el = [1, 1]

    r0 = [1,1]  # Введите радиус-вектор начала луча
    e = norm_v([1, -1])  # вектор направления луча
    n_r = [1, 0.8]  # кф преломления
    a = 3
    b = 2
    el = [1, 2]
    return r0, e, el, a, b, n_r

def check_ellipsoid():
    r0, e, el, a,b, n_r = testElips()
    t_e = intersection_with_ellipsoid(r0, e, el, a, b)
    print(t_e)
    if t_e is None:
        print('Конец работы функции')
    else:
        print("Длина луча ", t_e)
        cross_point = sphere.sum(r0, (mult(e, t_e)))
        print("Точка пересечения ", cross_point)

        p0_refl_e = sum(r0, mult(e,t_e))
        n = normal(cross_point[0],cross_point[1],a,b)
        print('normal ', n)

        e_refl_e = reflection_from_ellipsoid(e, n)
        print('e_refl_e', e_refl_e)
        p0_refr_e = p0_refl_e
        e_refr_e = refraction_after_ellipsoid(n_r, e, n)
        print('e_refr_e', e_refr_e)
        #
        plot_ellipsoid(el, a, b)
        plot_ray(r0, e, t_e, 'Исходный луч')
        plot_ray(p0_refl_e, e_refl_e, t_e, 'Отражённый луч')
        plot_ray(p0_refr_e, e_refr_e, t_e, 'Преломлённый луч')

        plt.legend(loc=1)
        plt.grid()
        plt.show()

def cheak_sphere():
    p0, R, r0, e, n_r = test()
    t = sphere.intersection_with_sphere(r0=r0, R=R, p0=p0, e=e)
    if t is None:
        print('Конец работы функции')
    else:
        print("Длина луча ", t)
        cross_point = sphere.sum(r0, (sphere.mult(e, t)))
        print("Точка пересечения ", cross_point)
        n_s = sphere.normal(r0=r0, e=e, p0=p0, t=t)
        print(n_s)
        # p0_refl_s = sphere.sum(r0, sphere.mult(e, t))
        # e_refl_s = sphere.reflection_from_sphere(e, n_s)
        # print('Отражение ', e_refl_s)
        #
        # p0_refr_s = p0_refl_s
        # e_refr_s = sphere.refraction_after_sphere(n_r, e, n_s)
        # print('Преломленный', e_refr_s)

        sphere.plot_sphere(p0, R)
        sphere.plot_ray(r0, e, t, 'Исходный луч')
        # sphere.plot_ray(p0_refl_s, e_refl_s, t, 'Отражённый луч')
        # sphere.plot_ray(p0_refr_s, e_refr_s, R, 'Преломлённый луч')
        plt.legend(loc=1)
        plt.grid()
        plt.show()

if __name__ == '__main__':
    check_ellipsoid()
    # cheak_sphere()