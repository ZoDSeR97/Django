from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(request, 'index.html')

def create_character(request):
    return render(request, 'create_character.html')