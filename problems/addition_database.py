from trainer.models import Problem, ProblemInstance

#generates the database of single and 2 digit addition problems
def gen_problems():
    for i in range(1,100,1):
        for j in range(1,100,1):
            variables = ','.join([str(i),str(j)])

            problem = Problem.objects.get(name='Addition')
            record = ProblemInstance(problem = problem, variables = variables)
            record.save()

def delete_problems():
    records = ProblemInstance.objects.filter(problem__name="Addition")
    records.delete()