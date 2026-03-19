from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/home.html')

@login_required
def grade12index(request):
    return render(request, "home/grade12index.html")
""" 
@login_required
def garde12SciecneIndex(request):
    context = {"list":[1,2,3,4,5]}
    return render(request, 'home/grade12ScienceIndex.html', context) """