import graphs as graph
import tables as table
from functions import *
from methods import *


def main():
    table.AnalyticData()

    xs1 = {
        't1': Rosenbrock(f1, const.x0['t1'], const.interval),
        't2': Rosenbrock(f1, const.x0['t2'], const.interval)
    }

    xs2 = {
        't1': Rosenbrock(f2, const.x0['t1'], const.interval),
        't2': Rosenbrock(f2, const.x0['t2'], const.interval)
    }

    table.ResultData(f1, xs1['t1'], xs1['t2'], name = 'Function 1')
    table.ResultData(f2, xs2['t1'], xs2['t2'], name = 'Function 2')

    table.FunctionData(f1, xs1['t1'], xs1['t2'], name = 'Function 1')
    table.FunctionData(f2, xs2['t1'], xs2['t2'], name = 'Function 2')

    graph.Xk(xs1['t1'], xs1['t2'], name = 'Function 1')
    graph.Xk(xs2['t1'], xs2['t2'], name = 'Function 2')

    graph.FunctionLevelRoute(f1, xs1['t1'], xs1['t2'], name = 'Function 1')
    graph.FunctionK(f1, xs1['t1'], xs1['t2'], func_num = 1, name = 'Function 1')

    graph.FunctionLevelRoute(f2, xs2['t1'], xs2['t2'], axis = 'vertical', name = 'Function 2')
    graph.FunctionK(f2, xs2['t1'], xs2['t2'], func_num = 2, name = 'Function 2')


if __name__ == '__main__':
    main()
