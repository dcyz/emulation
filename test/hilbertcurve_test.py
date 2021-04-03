from hilbertcurve.hilbertcurve import *
import random

if __name__ == '__main__':
    order = 10
    for i in range(100):
        x, y = random.randint(0, 1024), random.randint(0, 1024)
        d = point_to_hilbert(x, y, order)
        xi, yi = hilbert_to_point(d, order)
        if x == xi and y == yi:
            print('point [{:<4}, {:<4}] => distance {:<7}'.format(x, y, d), True)
        else:
            print('point [{:<4}, {:<4}] => distance {:<7}'.format(x, y, d), False)
            raise Exception('VERIFY ERROR')
