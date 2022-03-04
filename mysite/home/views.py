from django.shortcuts import render
from django.http import HttpResponse


TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)
def index(request):
    #return HttpResponse("Hello World. You are at home")
    return render(request, "index.html")
