from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import *
from .models import *
from .forms import *


def welcome(request):
    return render(request, 'panitsa/home.html')

def representative(request):
    representatives = Representative.objects.all().order_by('id')[:3]
    asom_representatives = Villagepublic.objects.all()[:10]
    print("Representatives:", representatives)
    print("Asom Representatives:", asom_representatives)
    return render(request, 'panitsa/representative.html', {'representatives': representatives, 'asom_representatives': asom_representatives})

def activity_news(request):
    activity_news = Activity_news.objects.all()
    return render(request, 'panitsa/activity_news.html',{'activity_news':activity_news})

def report_issue(request):
    return render(request, 'panitsa/report_issue.html')

def Income_expenses(request):
    return render(request, 'panitsa/income_expenses.html')

def donation_reportform(request):
    return render(request, 'panitsa/donation_report.html')

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_edit_view') 
    else:
        form = AdminLoginForm()

    return render(request, 'admin/login.html', {'form': form})


def edit_view(request):
    return render(request, 'admin/add_edit.html')

def add_representative(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('representative')  # เปลี่ยนเส้นทางไปที่หน้า 'representative' หลังจากบันทึก
    else:
        form = RepresentativeForm()

    return render(request, 'admin/add_representative.html', {'form': form})

def add_activity_news(request):
    if request.method == 'POST':
        form = Activity_newsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity_news')
    else:
        form = Activity_newsForm()

    return render(request, 'admin/add_activity_news.html',  {'form': form})

def add_villagepublic(request):
    if request.method == 'POST':
        form = VillagepublicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('representative')  # เปลี่ยนไปที่หน้า 'representative' หลังจากบันทึก
    else:
        form = VillagepublicForm()

    return render(request, 'admin/add_villagepublic.html', {'form': form})


def add_income_expenses(request):
    return render(request, 'admin/add_income_expenses.html')

