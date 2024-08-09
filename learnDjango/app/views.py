from django.shortcuts import render

# Create your views here.
def all_app(request):
    return render(request, 'UI/all_index.html')