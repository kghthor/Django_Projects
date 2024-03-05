# expense_tracker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Expense, UserProfile
from .forms import ExpenseForm, BudgetForm, IncomeForm

def home(request):
    return render(request,'registration/base.html')
 
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('expense_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('expense_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')

@login_required
def expense_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_tracker/expense_list.html', {'expenses': expenses, 'user_profile': user_profile})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            update_user_profile(request.user)
            messages.success(request, 'Expense added successfully.')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_tracker/add_expense.html', {'form': form})

@login_required
def budget_summary(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'expense_tracker/budget_summary.html', {'user_profile': user_profile})

@login_required
def set_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget updated successfully.')
            return redirect('budget_summary')
    else:
        form = BudgetForm(instance=request.user.userprofile)
    return render(request, 'expense_tracker/set_budget.html', {'form': form})

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income added successfully.')
            return redirect('budget_summary')
    else:
        form = IncomeForm(instance=request.user.userprofile)
    return render(request, 'expense_tracker/add_income.html', {'form': form})

def update_user_profile(user):
    user_profile = UserProfile.objects.get(user=user)
    expenses = Expense.objects.filter(user=user)
    total_spend = sum(expense.amount for expense in expenses)
    user_profile.total_spend = total_spend
    user_profile.save()
