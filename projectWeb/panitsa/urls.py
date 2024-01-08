from django.urls import path
from django.contrib.auth.views import *
from .views import *





urlpatterns = [
    path('', welcome, name='welcome'), 
    path('representative/', representative, name='representative'),
    path('activity_news/', activity_news, name='activity_news'),
    path('report_issue/', report_issue, name='report_issue'),
    path('income_expenses/', Income_expenses, name='income_expenses'),
    path('Donation_reportform/', donation_reportform, name='donation_reportform'),
    
    
    path('admin/login/', LoginView.as_view(), name='admin_login'),
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
    path('admin/add_representative/', add_representative, name='add_representative'),
    path('admin/add_edit/', edit_view, name='admin_edit'),
    path('admin/add_income_expenses/', add_income_expenses, name='add_income_expenses'),
    path('admin/add_villagepublic/', add_villagepublic, name='add_villagepublic'),
    path('add_activity_news/', add_activity_news, name='add_activity_news'), 


    
]