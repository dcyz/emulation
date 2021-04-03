_hilbert_map = {
    'a': {(0, 0): (0, 'd'), (0, 1): (1, 'a'), (1, 0): (3, 'b'), (1, 1): (2, 'a')},
    'b': {(0, 0): (2, 'b'), (0, 1): (1, 'b'), (1, 0): (3, 'a'), (1, 1): (0, 'c')},
    'c': {(0, 0): (2, 'c'), (0, 1): (3, 'd'), (1, 0): (1, 'c'), (1, 1): (0, 'b')},
    'd': {(0, 0): (0, 'a'), (0, 1): (3, 'c'), (1, 0): (1, 'd'), (1, 1): (2, 'd')},
}

_un_hilbert_map = {
    'a': {0: (0, 0, 'd'), 1: (0, 1, 'a'), 3: (1, 0, 'b'), 2: (1, 1, 'a')},
    'b': {2: (0, 0, 'b'), 1: (0, 1, 'b'), 3: (1, 0, 'a'), 0: (1, 1, 'c')},
    'c': {2: (0, 0, 'c'), 3: (0, 1, 'd'), 1: (1, 0, 'c'), 0: (1, 1, 'b')},
    'd': {0: (0, 0, 'a'), 3: (0, 1, 'c'), 1: (1, 0, 'd'), 2: (1, 1, 'd')}
}


def point_to_hilbert(x, y, order):
    current_square = 'a'
    position = 0
    for i in range(order - 1, -1, -1):
        position <<= 2
        quad_x = 1 if x & (1 << i) else 0
        quad_y = 1 if y & (1 << i) else 0
        quad_position, current_square = _hilbert_map[current_square][(quad_x, quad_y)]
        position |= quad_position
    return position


def hilbert_to_point(d, order):
    current_square = 'a'
    x = y = 0
    for i in range(order - 1, -1, -1):
        mask = 3 << (2 * i)
        quad_position = (d & mask) >> (2 * i)
        quad_x, quad_y, current_square = _un_hilbert_map[current_square][quad_position]
        x |= 1 << i if quad_x else 0
        y |= 1 << i if quad_y else 0
    return x, y
