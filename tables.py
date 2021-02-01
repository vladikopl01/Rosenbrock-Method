from scipy.optimize import fmin

from functions import *


def AnalyticData():
    analytic = [
        fmin(f1, const.x0['t1'], ftol = const.eps, full_output = True, disp = False),
        fmin(f2, const.x0['t1'], ftol = const.eps, full_output = True, disp = False)
    ]

    print('=' * 67)
    print("│ {:^63} │".format('Analytic solution'))
    print('=' * 67)
    print("│ {:^8s} │ {:^10s} │ {:^11s} │ {:^11s} │ {:^11s} │".
          format('Function', 'Iterations', 'x1', 'x2', 'F(x1, x2)'))
    print('=' * 67)

    for i in range(len(analytic)):
        print("│ {:8d} │ {:10} │ {:11.5} │ {:11.5} │ {:11.5} │".
              format(i + 1,
                     analytic[i][2],
                     analytic[i][0][0],
                     analytic[i][0][1],
                     analytic[i][1]))
        print('─' * 67)


def ResultData(func, xs1, xs2, name = 'Function'):
    print('=' * 67)
    print("│ {:^63} │".format(f'Minimize solution for {name}'))
    print('=' * 67)
    print("│ {:^8s} │ {:^10s} │ {:^11s} │ {:^11s} │ {:^11s} │".
          format('Start', 'Iterations', 'x1', 'x2', 'F(x1, x2)'))
    print('=' * 67)

    xs = [xs1.transpose()[-1], xs2.transpose()[-1]]
    result = [func(xs[0]), func(xs[1])]
    iterations = [len(xs1.transpose()) - 1, len(xs2.transpose()) - 1]

    for i in range(2):
        print("│ {:8d} │ {:10} │ {:11.5} │ {:11.5} │ {:11.5} │".
              format(i + 1,
                     iterations[i],
                     xs[i][0],
                     xs[i][1],
                     result[i]
                     )
              )
        print('─' * 67)


def FunctionData(f, xst1, xst2, name):
    xst1 = xst1.transpose()
    xst2 = xst2.transpose()
    print('=' * 91)
    print("│ {:^87} │".format(name))
    print('=' * 91)
    print("│ {:^3s} │ {:^39s} │ {:^39s} │".
          format(' ', 'Start point 1', 'Start point 2'))
    print("│ {:^3s} │{:s}│".format('K', '─' * 83))
    print("│ {:^3s} │ {:^11s} │ {:^11s} │ {:^11s} │ {:^11s} │ {:^11s} │ {:^11s} │".
          format(' ', 'F(x1, x2)', 'x1', 'x2', 'F(x1, x2)', 'x1', 'x2'))
    print('=' * 91)

    i = 0
    m = min(max(len(xst1), len(xst2)), const.table_max)
    while i < m:
        print("│ {:3d} │ {:11.5} │ {:11.5} │ {:11.5} │ {:11.5} │ {:11.5} │ {:11.5} │".
              format(i + 1,
                     f(xst1[i]) if 0 <= i < len(xst1) else ' ',
                     xst1[i][0] if 0 <= i < len(xst1) else ' ',
                     xst1[i][1] if 0 <= i < len(xst1) else ' ',
                     f(xst2[i]) if 0 <= i < len(xst2) else ' ',
                     xst2[i][0] if 0 <= i < len(xst2) else ' ',
                     xst2[i][1] if 0 <= i < len(xst2) else ' '))
        print('─' * 91)
        i += 1
