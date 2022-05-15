# koios

For cloning:

1. python manage.py createsuperuser
2. python manage.py makemigrations
3. python manage.py migrate
4. Create Problem models for the problems you want to showcase (e.g: Quadratic Equations) by visiting the admin site
5. python manage.py shell
6. from trainer.models import Problem, ProblemInstance
7. from problems.quadratic_equation import gen_problems_database
8. gen_problems_database()


Now the website should be functional, visit /train/quadratic_equation
