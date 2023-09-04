from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def About(request):
    return HttpResponse("<h1>About</h1>")

def Hello(request, username):
    #print(type(username))
    return HttpResponse("<h1>Hello %s</h1>" % username)