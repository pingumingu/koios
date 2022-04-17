from trainer.models import Problem, ProblemInstance

#generates the database of quadratic equations
def gen_problems():
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