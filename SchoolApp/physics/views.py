from django.shortcuts import render

# Create your views here.
def g12home(request):
    context = {"list":[1,2,3,4,5]}
    return render(request, 'physics/grade12/home.html', context)

def reading(request):
    context = {"list":[1,2,3,4,5]}
    return render(request, 'physics/grade12/fragments/reading.html', context)