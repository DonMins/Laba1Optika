import sphere
import matplotlib.pyplot as plt
import numpy as np

def test():
    p0 = [0, 0]  # Введите радиус-вектор центра сферы
    R = 4  # Радиус сферы
    r0 = [3, 1]  # Введите радиус-вектор начала луча
    e = sphere.norm_v([1, -1])  # вектор направления луча
    n_r = [1, 0.8]  # кф преломления
    return p0, R, r0, e, n_r


if __name__ == '__main__':
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
        p0_refl_s = sphere.sum(r0, sphere.mult(e, t))
        e_refl_s = sphere.reflection_from_sphere(e, n_s)
        print('Отражение ', e_refl_s)

        p0_refr_s = p0_refl_s
        e_refr_s = sphere.refraction_after_sphere(n_r, e, n_s)
        print('Преломленный', e_refr_s)

        sphere.plot_sphere(p0, R)
        sphere.plot_ray(r0, e, t, 'Исходный луч')
        sphere.plot_ray(p0_refl_s, e_refl_s, t, 'Отражённый луч')
        sphere.plot_ray(p0_refr_s, e_refr_s, R, 'Преломлённый луч')
        plt.legend(loc=1)
        plt.grid()
        plt.show()
