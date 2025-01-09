from django.shortcuts import render


# Create your views here.
def to_do_list(request):
    return render(request, 'todo.html')