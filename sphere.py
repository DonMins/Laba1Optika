import  numpy as np
import matplotlib.pyplot as plt

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


def intersection_with_sphere(r0, R, p0, e):
    temp =(scal_mult(sub(r0, p0), e)**2) - (scal_mult(sub(r0, p0), sub(r0, p0)) - R**2)
    if temp < 0:
        print('Луч не пересекает сферу')
    else:
        t1 = (scal_mult(sub(r0, p0), e)) - np.sqrt(temp)
        t2 = (scal_mult(sub(r0, p0), e)) + np.sqrt(temp)
        if t1 < 0:
            if t2 < 0:
                print('Луч не пересекает сферу')
            else:
                return t2
        elif t2 < 0:
            return t1
        else:
            return min(t1, t2)

def normal(r0, e, p0, t):
    temp = sub(sum(r0, mult(e, t)), p0)
    n = mult(temp,1 / np.sqrt(scal_mult(temp, temp)))
    n = norm_v(n)
    return n

def plot_sphere(p0, R):
    i = np.linspace(0, 2 * np.pi, 100)
    plt.plot(R * np.cos(i) + p0[0], R * np.sin(i) + p0[1])

def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1
def reflection_from_sphere(e, n):
    e_refl = sub(e, mult(n,2 * scal_mult(e, n)))
    e_refl = norm_v(e_refl)
    return e_refl

def refraction_after_sphere(n_refr, e, n):
    e_refr = sub(mult(e,n_refr[0]), mult(mult(n,sign(scal_mult(e, n))),n_refr[0] * abs(scal_mult(e, n)) -
    n_refr[1] * np.sqrt(1 - (n_refr[0] / n_refr[1])**2 * (1 - (scal_mult(e, n)**2)))))
    e_refr = mult(e_refr, 1 / n_refr[1])
    e_refr = norm_v(e_refr)
    return e_refr

def plot_ray(p0, e, t, name):
    j = np.linspace(0, t, 100)
    x = p0[0] + e[0] * j
    y = p0[1] + e[1] * j
    plt.plot(x, y, label=name)

def test():
    p0 = [0,2] # Введите радиус-вектор центра сферы
    r = 4 # Радиус сферы
    r0 = [3,3] # Введите радиус-вектор начала луча
    e = norm_v([1,-1]) #вектор направления луча
    n_r = [1, 2] #кф преломления
    return p0,r,r0,e, n_r

if __name__ == '__main__':
    p0,R,r0,e,n_r = test()
    t = intersection_with_sphere(r0, R, p0, e)
    if t is None:
        print('Конец работы функции')
    else:
        print("Длина луча ", t)
        cross_point = sum(p0, (mult(e, t)))
        print("Точка пересечения ", cross_point)
        n_s = normal(r0, e, p0, t)
        print(n_s)
        p0_refl_s = sum(p0, mult(e,t))
        e_refl_s = reflection_from_sphere(e, n_s)
        print('Отражение ', e_refl_s)

        p0_refr_s = p0_refl_s
        e_refr_s = refraction_after_sphere(n_r, e, n_s)
        print('Преломленный', e_refr_s)

        plot_sphere(p0, R)
        plot_ray(p0, e, t, 'Исходный луч')
        plot_ray(p0_refl_s, e_refl_s, t, 'Отражённый луч')
        plot_ray(p0_refr_s, e_refr_s, R, 'Преломлённый луч')
        plt.legend(loc=1)
        plt.grid()
        plt.show()


