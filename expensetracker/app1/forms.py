
from django import forms
from .models import Expense, UserProfile

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description', 'payment_method', 'receipt_image', 'location']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['budget']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['total_income']
