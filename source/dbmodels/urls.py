from django.urls import path
from . import views
app_name = "dbmodels"

urlpatterns = [
    path('student_detail/<int:pk>/', views.as_view(), name="student_detail")
]