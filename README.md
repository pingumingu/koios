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

Module adding workflow:

1. add python module in problems folder
2. create Problem in django admin
3. run gen_problems_database() as above

Resetting migrations:

1. Delete everything in migrations folder under every app except for __init__.py
2. Delete the database file db.sqlite3
3. After making changes, python manage.py makemigrations
4. python manage.py migrate