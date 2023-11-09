from django.http import HttpResponse
from AppCoder.models import Course


# Create your views here.
def create_course(request):
    curso = Course(name="Python", camada=47785)
    curso.save()

    return HttpResponse(curso.name)
