import constants as const


def f1(x):
    x1, x2 = x
    return (x1 - const.N)**2 + (10 * x2 - const.N)**2


def f2(x):
    x1, x2 = x
    return (const.N * x2 / 3 - x1**2)**2 + (const.N / 2 - x1)**2
