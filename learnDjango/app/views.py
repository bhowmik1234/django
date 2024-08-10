from django.shortcuts import render
from .models import varity, collage
from django.shortcuts import get_object_or_404
from .forms import varityForm

# Create your views here.
def all_app(request):
    names = varity.objects.all()
    return render(request, 'UI/all_index.html', {'names': names})

def desp(request, id):
    name = get_object_or_404(varity, pk=id)
    return render(request, 'UI/desp.html', {'names': name})

def store(request):
    collages = None
    if request.method == 'POST':
        form = varityForm(request.POST)
        if form.is_valid():
            variety_form = form.cleaned_data['varity_form']
            collages = collage.objects.filter(collage=variety_form)
    else:
        forms = varityForm()
    return render(request, 'UI/store.html', {'collages': collages, 'form': forms})