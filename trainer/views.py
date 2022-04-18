from django.shortcuts import render

# Create your views here.
from .models import Tag, Problem, ProblemInstance, TimeTaken

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_problems = Problem.objects.all().count()
    num_instances = ProblemInstance.objects.all().count()
    num_solves = TimeTaken.objects.all().count()

    context = {
        'num_problems': num_problems,
        'num_instances': num_instances,
        'num_solves': num_solves,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

import random
#base_problem is passed through the URL
def train(request, base_problem):
    """
    View function for training a specific problem
    """

    #takes in the base_problem passed from the url , eg: quadratic_equation, and converts it to the Problem name to pass to the database query.
    base_problem = ' '.join([i.capitalize() for i in base_problem.split('_')])

    problem_instances = list(ProblemInstance.objects.filter(problem__name = base_problem))
    random_items = random.sample(problem_instances, 5)
    problem_list = [problem.get_problem_solution_data() for problem in random_items]

    context = {
        'problem_list': problem_list,
        'base_problem' : base_problem,
    }

    return render(request, 'train.html', context = context)
    