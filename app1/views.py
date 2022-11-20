from django.shortcuts import redirect, render
from app1.models import Student
from app1.forms import StudentForm

# Create your views here.
def student_View(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')

    context = {'form': form}
    return render(request, template_name, context)

def showStudent_View(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'data': data}
    return render(request, template_name, context)