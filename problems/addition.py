import numpy as np
from fractions import Fraction

def gen_problem(variables, id):
    variables = variables.split(',')
    a = int(variables[0])
    b = int(variables[1])
    problem = f'\({a} + {b}\)'
    solution = a + b

    return {'id': id,
        'problem': problem,
        'solution' : str(solution),
        'worked_solution' : str(solution)}
