from django.urls import path
from app1.views import student_View, showStudent_View

urlpatterns = [
    path('sv/', student_View, name="student_url"),
    path('ss/', showStudent_View, name="showstudent_url"),

]