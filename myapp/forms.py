from django import forms
from .models import Work

class WorkCreate(forms.ModelForm):
    class Meta:
        model=Work
        fields='__all__'
