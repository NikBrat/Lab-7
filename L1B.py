import numpy as np
import random as rnd
from time import perf_counter
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


def time_comparison():
    # Время простых списков

    # Начальное время
    t1_start = perf_counter()

    # Генерация списков и поэдементное умножение
    a1 = [rnd.randint(-25, 35) for s in range(10 ** 6)]
    b1 = [rnd.randint(-25, 35) for s in range(10 ** 6)]
    result = [x * y for x, y in zip(a1, b1)]

    # Конечое время
    t1_stop = perf_counter()

    t1_final = t1_stop - t1_start
    print(f'Затраченное время при использовании списков:\n {t1_final}')

    # Время массивов numpy

    t2_start = perf_counter()
    a2 = np.random.randint(-25, 35, size=10 ** 6)
    b2 = np.random.randint(-25, 35, size=10 ** 6)
    np.multiply(a2, b2)
    t2_stop = perf_counter()

    t2_final = t2_stop - t2_start
    print(f'\nЗатраченное время при использовании массивов numpy:\n {t2_final}')

    if t2_final < t1_final:
        print('\nNumpy быстрее :)')


def histogram():
    # Построение гистограммы
    arr = np.genfromtxt('data2.csv', delimiter=',')
    arr = arr[1:]
    hardness = np.array(arr[:, 1], float)
    hardness = hardness[~np.isnan(hardness)]
    fig = plt.figure(figsize=(24.0, 11.0))
    ax = plt.subplot(1, 2, 1)
    ax.hist(hardness, 55, (50, 350), color='red', ec='green')
    ax.grid()
    ax.set_title('Гистограмма')
    ax.set_xlabel('Hardness')
    ax.set_ylabel('Частота')

    # Построение нормализованной гистограммы
    ax1 = plt.subplot(1, 2, 2)
    ax1.hist(hardness, 55, (50, 350), color='yellow', ec='red', density=True)
    ax1.grid()
    ax1.set_title('Нормализованная гистограмма')
    ax1.set_xlabel('Hardness')
    ax1.set_ylabel('Частота')
    plt.show()
    print('\nCреднеквадратичное отклонение:\n', np.std(hardness))


def d3graphic():
    np.random.seed(28)
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(x ** y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_wireframe(x, y, z, color="gray")
    plt.title('3D  график sin(x^y)')
    plt.show()


def animation():
    fig = plt.figure()
    l, = plt.plot([], [])
    plt.xlim(-7, 7)
    plt.ylim((-1.5, 1.5))

    def function(t):
        return np.sin(t)

    writer = PillowWriter(fps=15)

    xval = []
    yval = []

    with writer.saving(fig, "sin_function.gif", 100):
        for x in np.linspace(-10, 10, 100):
            xval.append(x)
            yval.append(function(x))
            l.set_data(xval, yval)
            writer.grab_frame()


if __name__ == '__main__':
    time_comparison()
    histogram()
    d3graphic()
    animation()
