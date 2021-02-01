import matplotlib.pyplot as plt
from numpy import linspace, meshgrid, arange

import constants as const


def FunctionLevelRoute(f, xst1, xst2, axis = 'horizontal', name = None):
    x = linspace(const.interval['x1'][0] * 1.5, const.interval['x1'][1] * 1.5, 1000)
    y = linspace(const.interval['x2'][0] * 1.5, const.interval['x2'][1] * 1.5, 1000)

    X, Y = meshgrid(x, y)
    Z = f([X, Y])

    levels = linspace(
        min(min(f([xst1[0], xst1[1]])), min(f([xst2[0], xst2[1]]))),
        max(max(f([xst1[0], xst1[1]])), max(f([xst2[0], xst2[1]]))),
        const.levels
    )

    fig = plt.figure()
    fig.suptitle(name)

    # T1 contour
    plt.subplot(1, 2, 1) if axis == 'horizontal' else plt.subplot(2, 1, 1)
    plt.xlabel('X1')
    plt.ylabel('X2')

    plt.plot(xst1[0], xst1[1], 'o--', color = 'magenta', label = 'Route for T1', zorder = 5)
    plt.plot(xst2[0], xst2[1], 'o--', color = 'blueviolet', alpha = 0.3, label = 'Route for T2', zorder = 4)

    plt.contour(X, Y, Z, levels, colors = 'purple', zorder = 3)
    plt.contourf(X, Y, Z, levels, cmap = 'RdPu', zorder = 2, alpha = 0.7)

    plt.legend()
    plt.grid(zorder = 1)

    # T2 contour
    plt.subplot(1, 2, 2) if axis == 'horizontal' else plt.subplot(2, 1, 2)
    plt.xlabel('X1')
    plt.ylabel('X2')

    plt.plot(xst1[0], xst1[1], 'o--', color = 'magenta', alpha = 0.3, label = 'Route for T1', zorder = 4)
    plt.plot(xst2[0], xst2[1], 'o--', color = 'blueviolet', label = 'Route for T2', zorder = 5)

    plt.contour(X, Y, Z, levels, colors = 'purple', zorder = 3)
    contourf = plt.contourf(X, Y, Z, levels, cmap = 'RdPu', zorder = 2, alpha = 0.7)

    plt.legend()
    plt.grid(zorder = 1)

    fig.subplots_adjust(right = 0.85)
    colorbar_ax = fig.add_axes([0.9, 0.15, 0.025, 0.7])
    fig.colorbar(contourf, cax = colorbar_ax)

    plt.show()


def Xk(xst1, xst2, name = None):
    x1_t1 = xst1[0]
    x2_t1 = xst1[1]
    K_t1 = range(len(x1_t1))

    plt.figure().suptitle(name)

    # X1 T1 graph
    plt.subplot(2, 2, 1)
    plt.xlabel('K')
    plt.ylabel('X1')
    plt.title('X1 steps for T1')
    plt.grid()
    if len(K_t1) < 10:
        plt.xticks(arange(len(x1_t1), step = 1))

    plt.plot(K_t1, x1_t1, 'o--')
    plt.plot(K_t1, x2_t1, 'ko--', color = 'grey', alpha = 0.3)
    plt.legend(['X1', 'X2'])

    # X2 T1 graph
    plt.subplot(2, 2, 2)
    plt.xlabel('K')
    plt.ylabel('X2')
    plt.title('X2 steps for T1')
    plt.grid()
    if len(K_t1) < 10:
        plt.xticks(arange(len(x2_t1), step = 1))

    plt.plot(K_t1, x2_t1, 'o--')
    plt.plot(K_t1, x1_t1, 'o--', color = 'grey', alpha = 0.3)
    plt.legend(['X2', 'X1'])

    x1_t2 = xst2[0]
    x2_t2 = xst2[1]
    K_t2 = range(len(x1_t2))

    # X1 T2 graph
    plt.subplot(2, 2, 3)
    plt.xlabel('K')
    plt.ylabel('X1')
    plt.title('X1 steps for T2')
    plt.grid()
    if len(K_t2) < 10:
        plt.xticks(arange(len(x1_t2), step = 1))

    plt.plot(K_t2, x1_t2, 'o--')
    plt.plot(K_t2, x2_t2, 'ko--', color = 'grey', alpha = 0.3)
    plt.legend(['X1', 'X2'])

    # X2 T2 graph
    plt.subplot(2, 2, 4)
    plt.xlabel('K')
    plt.ylabel('X2')
    plt.title('X2 steps for T2')
    plt.grid()
    if len(K_t2) < 10:
        plt.xticks(arange(len(x2_t2), step = 1))

    plt.plot(K_t2, x2_t2, 'o--')
    plt.plot(K_t2, x1_t2, 'o--', color = 'grey', alpha = 0.3)
    plt.legend(['X2', 'X1'])

    plt.show()


def Xs(xs, name = None):
    plt.xlabel('Xs2')
    plt.ylabel('Xs1')
    plt.title(name)
    plt.grid()

    plt.plot(xs[1], xs[0], 'o-')
    plt.legend([f'X steps'])

    plt.show()


def FunctionK(f, xst1, xst2, func_num, name = None):
    func_t1 = [f([xst1[0][i], xst1[1][i]]) for i in range(len(xst1[0]))]
    K_t1 = range(len(func_t1))

    func_t2 = [f([xst2[0][i], xst2[1][i]]) for i in range(len(xst2[0]))]
    K_t2 = range(len(func_t2))

    plt.figure().suptitle(name)
    # T2 graph
    plt.subplot(1, 2, 1)
    plt.xlabel('K')
    plt.ylabel('F(x1, x2)')
    plt.grid()

    plt.plot(K_t1, func_t1, 'mo-')
    plt.plot(K_t2, func_t2, 'mo-', alpha = 0.3)
    plt.legend(['Function values for T1',
                'Function values for T2'])

    # T2 graph
    plt.subplot(1, 2, 2)
    plt.xlabel('K')
    plt.ylabel('F(x1, x2)')
    plt.grid()

    plt.plot(K_t1, func_t1, 'mo-', alpha = 0.3)
    plt.plot(K_t2, func_t2, 'mo-')
    plt.legend([f'Function values for T1',
                f'Function values for T2'])

    plt.show()


def Fk(f1, xs1, f2, xs2):
    tmp_func1 = [f1([xs1[0][i], xs1[1][i]]) for i in range(1, len(xs1[0]))]
    tmp_func2 = [f2([xs2[0][i], xs2[1][i]]) for i in range(1, len(xs2[0]))]

    if len(tmp_func1) < len(tmp_func2):
        for i in range(len(tmp_func1), len(tmp_func2)):
            tmp_func1.append(tmp_func1[-1])
    elif len(tmp_func2) < len(tmp_func1):
        for i in range(len(tmp_func2), len(tmp_func1)):
            tmp_func2.append(tmp_func2[-1])

    K = range(max(len(tmp_func1), len(tmp_func2)))

    # F1 graph
    plt.subplot(1, 2, 1)
    plt.xlabel('K')
    plt.ylabel('Function 1')
    plt.title('Function 1 values')
    plt.grid()

    plt.plot(K, tmp_func1, 'mo--')
    plt.plot(K, tmp_func2, 'ko--', color = 'grey', alpha = 0.3)
    plt.legend(['Function 1', 'Function 2'])

    # F2 graph
    plt.subplot(1, 2, 2)
    plt.xlabel('K')
    plt.ylabel('Function 2')
    plt.title('Function 2 values')
    plt.grid()

    plt.plot(K, tmp_func2, 'mo--')
    plt.plot(K, tmp_func1, 'o--', color = 'grey', alpha = 0.3)
    plt.legend(['Function 2', 'Function 1'])

    plt.show()
