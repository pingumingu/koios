import numpy as np
from fractions import Fraction

def gen_problem(variables, id):
    variables = variables.split(',')
    a = int(variables[0])
    b = int(variables[1])
    c = int(variables[2])
    problem = f'\({a}x^2 + {b}x + {c} = 0\)'
    solution_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    solution_1 = Fraction(solution_1).limit_denominator(20)
    solution_2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    solution_2 = Fraction(solution_2).limit_denominator(20)
    return {'id': id, 'problem': problem,  'solution' : f'x = {str(solution_1)}, x = {str(solution_2)}', 'worked_solution' : f'x = {str(solution_1)}, x = {str(solution_2)}'}

from trainer.models import Problem, ProblemInstance

#generates the database of quadratic equations
def gen_problems_database():
    for i in range(-10,11,1):
        for j in range(-10,11,1):
            for k in range(-10,11,1):
                for l in range(-10,11,1):
                    
                    a = i*k
                    b = (j*k) + (i*l)
                    c = j*l
                    
                    if a<9 and a>-9 and a!=0:
                        problem = Problem.objects.get(name='Quadratic Equation')
                        record = ProblemInstance(problem = problem, variables = ','.join([str(a),str(b),str(c)]))
                        record.save()

def delete_problems():
    records = ProblemInstance.objects.all()
    records.delete()