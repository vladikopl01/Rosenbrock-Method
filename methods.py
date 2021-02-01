from numpy import append, array, fabs, sqrt, zeros, copy

import constants as const


def GoldenSection(f, xs, index, a, b):
    g_param = (sqrt(5) - 1) / 2.

    p = a + (1 - g_param) * (b - a)
    q = a + g_param * (b - a)

    xs[index] = p
    tmpA = f(xs)

    xs[index] = q
    tmpB = f(xs)

    k = 1
    while k <= const.max_iter and fabs(b - a) > const.eps:
        if tmpA < tmpB:
            b = q
            q = p
            tmpB = tmpA
            p = a + (1 - g_param) * (b - a)
            xs[index] = p
            tmpA = f(xs)
        else:
            a = p
            p = q
            tmpA = tmpB
            q = a + g_param * (b - a)
            xs[index] = q
            tmpB = f(xs)
        xs[index] = fabs((b + a) / 2)
        k += 1
    return (a + b) / 2


def CountNewX(start_x, x, sin, cos):
    return [
        start_x[0] + x[0] * sin - x[1] * cos,
        start_x[1] + x[0] * cos + x[1] * sin
    ]


def Rosenbrock(f, start_x, interval):
    cur_x = array([start_x])

    delta_x = 0
    delta_y = 0
    cos = 0
    sin = 0
    temp_x = 0
    tmpB = f(start_x)
    x_new = zeros(2)
    x = zeros(2)
    new_start_x = copy(start_x)

    k = 1
    while k <= const.max_iter:
        tmpA = tmpB
        start_x = copy(start_x)

        for index in range(2):
            new_start_x[index] = GoldenSection(
                f, copy(new_start_x), index,
                interval[f'x{index + 1}'][0],
                interval[f'x{index + 1}'][1]
            )

            if delta_x > 0 and delta_y > 0:
                if index == 0:
                    x[0] = (new_start_x[0] - start_x[0]) * sin + (new_start_x[1] - start_x[1]) * -cos
                    temp_x = x[0]
                    x[1] = 0
                elif index == 1:
                    x[0] = temp_x
                    x[1] = (new_start_x[1] - start_x[1]) * sin - (new_start_x[0] - start_x[0]) * -cos
                x_new = CountNewX(start_x, x, sin, -cos)
            elif delta_x > 0 and delta_y < 0:
                if index == 0:
                    x[0] = (new_start_x[0] - start_x[0]) * -sin + (new_start_x[1] - start_x[1]) * -cos
                    temp_x = x[0]
                    x[1] = 0
                elif index == 1:
                    x[0] = temp_x
                    x[1] = (new_start_x[1] - start_x[1]) * -sin - (new_start_x[0] - start_x[0]) * -cos
                x_new = CountNewX(start_x, x, -sin, -cos)
            elif delta_x < 0 and delta_y < 0:
                if index == 0:
                    x[0] = (new_start_x[0] - start_x[0]) * -sin + (new_start_x[1] - start_x[1]) * cos
                    temp_x = x[0]
                    x[1] = 0
                elif index == 1:
                    x[0] = temp_x
                    x[1] = (new_start_x[1] - start_x[1]) * -sin - (new_start_x[0] - start_x[0]) * cos
                x_new = CountNewX(start_x, x, -sin, cos)
            elif delta_x < 0 and delta_y > 0:
                if index == 0:
                    x[0] = (new_start_x[0] - start_x[0]) * sin + (new_start_x[1] - start_x[1]) * cos
                    temp_x = x[0]
                    x[1] = 0
                elif index == 1:
                    x[0] = temp_x
                    x[1] = (new_start_x[1] - start_x[1]) * sin - (new_start_x[0] - start_x[0]) * cos
                x_new = CountNewX(start_x, x, sin, cos)

        new_start_x = copy(x_new)

        tmpB = f(new_start_x)
        if fabs(tmpA - tmpB) < const.eps:
            break

        delta_x = new_start_x[0] - start_x[0]
        delta_y = new_start_x[1] - start_x[1]

        sin = fabs(delta_y) / sqrt(delta_y**2 + delta_x**2)
        cos = fabs(delta_x) / sqrt(delta_y**2 + delta_x**2)

        cur_x = append(cur_x, [new_start_x], axis = 0)
        k += 1
    return cur_x.transpose()
