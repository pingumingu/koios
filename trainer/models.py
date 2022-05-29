from django.db import models
from django.urls import reverse
import importlib
# Create your models here.

class Tag(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a tag name(s) (e.g. Maths, Year 7, Functions)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Problem(models.Model):
    """
    Model representing a 'base' problem
    """
    name = models.CharField(max_length = 50, help_text = 'Enter the name of the base problem (e.g. Quadratic Equation)')

    tag = models.ManyToManyField(Tag, help_text = 'Select tags for this problem')
    
    problem_module = models.CharField(max_length = 100, help_text = 'eg: koios_webapp.problems.quadratic_trainer')
    problem_function = models.CharField(max_length = 100, help_text = "gen_problem")

    def __str__(self):
        """
        String for repreenting the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """Returns the URL to the training page for this Problem."""
        return reverse('train', args=['_'.join(self.name.split(' ')).lower()])

    def display_tag(self):
        """Create a string for the first 3 Tags. This is required to display multiple tags in Admin."""
        return ', '.join(tag.name for tag in self.tag.all()[:3])

    display_tag.short_description = 'Tag'


import uuid # Required for unique problem instances
 
class ProblemInstance(models.Model):
    """
    Model for representing a generated problem from base problem.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular generated problem across whole application')

    #null=True allows the database to stoer a Null value if no base Problem is selected, we don't want this
    #on_delete=models.PROTECT prevents the base problem from being deleted as long as it is referenced by a Problem Instance.
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT, null=False)
    variables = models.CharField(max_length = 100, help_text = 'Enter the variables separated by commas')

    def get_problem_solution_data(self):
        module_name = self.problem.problem_module
        #takes koios_webapp.problems.quadratic_equation and turns into problems.quadratic_equation
        #when the runserver is run, it runs from the outer koios_webapp directory, so we import relative
        #to that directly i.e. import problems.quadratic_equation
        module_name = '.'.join(module_name.split('.')[1:3])
        function_name = self.problem.problem_function
        module = importlib.import_module(module_name)
        return getattr(module, function_name)(self.variables,self.id)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)

class TimeTaken(models.Model):
    """
    Model for representing how long it takes for someone to solve a particular problem instance
    """

    problem_instance = models.ForeignKey(ProblemInstance, on_delete=models.PROTECT, null=False)
    time = models.FloatField()