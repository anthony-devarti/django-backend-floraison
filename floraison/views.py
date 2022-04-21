from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("You're at the bakery index.")