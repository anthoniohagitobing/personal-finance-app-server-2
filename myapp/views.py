from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    return render(request, "home.html")
        # this wil render you the templates
        # This only works if the template is in the templates directory

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})