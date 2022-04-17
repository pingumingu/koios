from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #re_path for when using regular expressions
    re_path(f'^(?P<base_problem>\w+)$', views.train, name = 'train'),
]

