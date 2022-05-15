import numpy as np
from fractions import Fraction

def gen_problem(variables, id):
    variables = variables.split(',')

    if int(variables[0]) > int(variables[1]):
        a = int(variables[0])
        b = int(variables[1])
    else:
        a = int(variables[1])
        b = int(variables[0])

    problem = f'\({a} - {b}\)'
    solution = a - b

    return {'id': id,
        'problem': problem,
        'solution' : str(solution),
        'worked_solution' : str(solution)}

from trainer.models import Problem, ProblemInstance

#generates the database of single and 2 digit subtraction problems
def gen_problems_database():
    for i in range(1,100,1):
        for j in range(1,100,1):
            variables = ','.join([str(i),str(j)])

            problem = Problem.objects.get(name='Subtraction')
            record = ProblemInstance(problem = problem, variables = variables)
            record.save()

def delete_problems():
    records = ProblemInstance.objects.filter(problem__name="Subtraction")
    records.delete()