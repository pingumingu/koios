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
