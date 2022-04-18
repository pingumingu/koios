import numpy as np

def gen_problem(variables, id):
    variables = variables.split(',')
    a = int(variables[0])
    b = int(variables[1])
    c = int(variables[2])
    problem = f'{a}x^2 + {b}x + {c}=0'
    solution_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    solution_2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    return {'id': id, 'problem': problem,  'solution' : f'x = {str(solution_1)}, x = {str(solution_2)}', 'worked_solution' : f'x = {str(solution_1)}, x = {str(solution_2)}'}
