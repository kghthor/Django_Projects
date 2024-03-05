from .models import Information
from django import forms


class Informationform(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['name','email','mobile']
        labels = {
            'name': '',
              'email': '',
                'mobile': '',
        }
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Name'}),
              'email': forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Email'}),
               'mobile': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Mobile'}),
        }
      

