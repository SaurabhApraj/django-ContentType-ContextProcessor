from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp_one/index.html')

def student(request):
    return render(request, 'myapp_one/students.html')