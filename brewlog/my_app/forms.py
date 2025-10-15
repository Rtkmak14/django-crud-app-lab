from django import forms
from .models import Tasting

class TastingForm(forms.ModelForm):
    class Meta:
        model=Tasting
        fields = '__all__'

