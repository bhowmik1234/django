from django import forms
from .models import varity

class varityForm(forms.Form):
    varity_form = forms.ModelChoiceField(queryset=varity.objects.all(), label='select varity')
    # vart = forms.CharField()