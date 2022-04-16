from django.db import models
from django.urls import reverse
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

    problem_text = models.TextField(max_length = 2000,
        help_text = 'Enter the text for the problem, with the variables separated by spaces named !var!')
    solution_text = models.TextField(max_length = 10000,
        help_text = 'Enter the text for the worked solution, with the variables separated by spaces named !var!')

    def __str__(self):
        """
        String for repreenting the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Problem."""
        return reverse('problem-detail', args=[str(self.id)])

#class ProblemSolutionText(models.Model):
#    """
#    Model representing the problem and solution text of a 'base problem'
#    """
#    #if A has a B, then B should have the one-to-one field
#    problem = models.OneToOneField(Problem, help_text = 'Select the problem for this problem/solution text set')
#
#    problem_text = models.TextField(max_length = 2000,
#        help_text = 'Enter the text for the problem, with the variables separated by spaces named !var!')
#    solution_text = models.TextField(max_length = 10000,
#        help_text = 'Enter the text for the worked solution, with the variables separated by spaces named !var!')
#
#    def __str__(self):
#        """
#        String for representing the Model object.
#        """
#        return f'problem/solution text of {self.problem.name}'
#
#    def get_fstring(self):
#        """
#        Return the """

    
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

    def get_problem_text_instance(self):
        problem_text_instance = self.problem.problem_text
        problem_text_instance_list = problem_text_instance.split('!var!')
        variable_list = self.variables.split(',')
        return ''.join([i + j for i,j in zip(problem_text_instance_list, variable_list)])

    def get_solution_text_instance():


    