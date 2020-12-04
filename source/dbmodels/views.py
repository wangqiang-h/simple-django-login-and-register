from django.views.generic import View, ListView, DetailView
from . import models

class StudentView(DetailView):
    model = models.Student
    template_name = 'dbmodels/student_detail.html'


