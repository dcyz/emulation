from rappor.rappor import *
from time import *


def timer(func):
    def run(*args):
        start = perf_counter_ns()
        result = func(*args)
        end = perf_counter_ns()
        print('Time:', (end - start) / 1000000, 'ms')
        return result

    return run


@timer
def test():
    r = Rappor(12)
    return r


if __name__ == '__main__':
    Rappor.setup(10000)
    rappor = test()
    print(rappor.get_value())
