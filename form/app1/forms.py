from django import forms
from .models import customer
class customerform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
        #fields=['name','email']