from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return HttpResponse("<h1>About</h1>")

def Hello(request, username):
    #print(type(username))
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    #task = Task.objects.get(name=name)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)