from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
   home, register_view, login_view, logout_view,
    expense_list, add_expense, budget_summary,
    set_budget, add_income
)
urlpatterns = [
    path('',home,name="home"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('expenses/', expense_list, name='expense_list'),
    path('add_expense/', add_expense, name='add_expense'),
    path('budget_summary/', budget_summary, name='budget_summary'),
    path('set_budget/', set_budget, name='set_budget'),
    path('add_income/', add_income, name='add_income'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
