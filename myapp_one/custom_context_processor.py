from .models import Student

def student_renderer(request):
    data = {
        'students': Student.objects.all(),
    }
    return data