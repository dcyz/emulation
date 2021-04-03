from rappor.rappor import Rappor
from rappor.stat import *
from hilbertcurve.hilbertcurve import *
import matplotlib.pyplot as plt
import random
import numpy as np

# 这里假设Hilbert曲线迭代三次
order = 3
n = 4 ** order
w = 2 ** order


def distance_gen_average():
    return random.randint(0, n - 1)


def distance_gen_normal():
    r, d = random.random(), 0
    if r < 0.2:
        d = n / 4 + 0.5 * np.random.randn()
    elif r < 0.8:
        d = n / 2 + 0.5 * np.random.randn()
    elif r < 1:
        d = 3 * n / 4 + 0.5 * np.random.randn()
    return d


def point_gen_average():
    return random.random() + random.randint(0, w - 1), random.random() + random.randint(0, w - 1)


def point_gen_normal():
    c = random.random()
    if c < 0.2:
        return np.random.randn() * 0.25 + w / 4, np.random.randn() * 0.25 + w / 4
    elif c < 0.8:
        return np.random.randn() * 0.25 + w / 2, np.random.randn() * 0.25 + w / 2
    elif c < 1:
        return np.random.randn() * 0.25 + w * 3 / 4, np.random.randn() * 0.25 + w * 3 / 4


def test():
    us, list_actual, list_stat = [], [0 for i in range(n)], [0 for i in range(n)]
    points_x, points_y = [], []
    total = n * 100

    Rappor.setup(n, f=0, p=0.25, q=0.75)
    for i in range(total):
        # loc = distance_gen_average()
        # loc = distance_gen_normal()
        x, y = 0, 0
        # 这里我用0.5概率生成平均分布点，0.5概率生成聚集在三个位置的正态分布点
        if i < 0.5 * total:
            x, y = point_gen_normal()
        else:
            x, y = point_gen_average()
        # 先把坐标转换成整数，然后进行Hilbert曲线的转换
        loc = point_to_hilbert(round(x), round(y), order)
        # 计算实际点位分布密度
        list_actual[loc] += 1
        # 添加RAPPOR响应数组
        us.append(Rappor(loc).get_value())
        points_x.append(x)
        points_y.append(y)
    # 获取统计结果
    s = Stat(us)
    list_stat = s.get_result()
    print(list_stat)

    # show the points and simulation's result
    plt.figure()

    # 实际点位的散点图，有三个聚集点
    plt.subplot(1, 2, 1)
    plt.scatter(points_x, points_y, marker='.', s=0.01)

    # 统计折线图，蓝色是实际分布，红色是统计分布
    x_list = [i for i in range(n)]
    plt.subplot(1, 2, 2)
    plt.plot(x_list, list_actual, color='blue')
    plt.plot(x_list, list_stat, color='red')

    plt.show()


if __name__ == '__main__':
    test()
