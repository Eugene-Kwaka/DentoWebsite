from newsletter.models import Signup
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.mail import send_mail
from django.conf import settings


from newsletter.models import Signup
from blog.models import Post
from dentist.models import *
from .forms import *


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users


# Create your views here.


# REGISTRATION AND USER AUTHERNTICATION VIEWS

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            return redirect('loginPage')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username OR Password is incorrect!")

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def home(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    services = Service.objects.all()
    context = {
        'latest': latest,
        'services': services,
    }
    return render(request, 'home.html', context)


@login_required(login_url='loginPage')
def book_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = Appointment(
                user=request.user,
                name=request.POST['name'], 
                phone=request.POST['phone'], 
                email=request.POST['email'], 
                schedule=request.POST['schedule'], 
                date=request.POST['date'], 
                message=request.POST['message']
                )
            appointment.save()
            messages.success(request, f"Appointment booked successfully.")
            # return redirect('confirmappointment', pk=appointment.id)
            return redirect('my_appointments')
        else:
            form = AppointmentForm()

    context = {
        'form': form,
    }
    return render(request, 'book_appointment.html', context)

@login_required(login_url='loginPage')
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    context={
        'appointments':appointments,
    }
    return render(request, 'my_appointments.html', context)

@login_required(login_url='loginPage')
def update_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('my_appointments')
    context = {
        'form': form,
    }
    return render(request, 'update_appointment.html', context)

@login_required(login_url='loginPage')
def delete_appointment(request, pk):
    appointment= Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('my_appointments')
    context = {
        'appointment': appointment,
    }
    return render(request, 'delete_appointment.html', context)
# @login_required(login_url='loginPage')
# def confirm_appointment(request,pk):
#     appointment = get_object_or_404(Appointment, id=pk)
#     context = {
#         'appointment': appointment,
#     }
#     return render(request, 'confirm_appointment.html', context)


def pricing(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'pricing.html', context)


def service(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }

    return render(request, 'service.html', context)


@allowed_users(allowed_roles=['admin'])
def create_service(request):
    form = ServiceForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = ServiceForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('pricing')
    context = {
        'form': form,
    }

    return render(request, 'set_services.html', context)


@allowed_users(allowed_roles=['admin'])
def update_service(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service')

    context = {
        'form': form,
    }
    return render(request, 'update_services.html', context)


@allowed_users(allowed_roles=['admin'])
def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service')

    context = {
        'service': service,
    }
    return render(request, 'delete_services.html', context)


def pricing(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'pricing.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            send_mail(f"{contact_name} sent an email", contact_message,
                      contact_email, [settings.EMAIL_HOST_USER], fail_silently=False)
            return redirect('email')

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)


def email(request):
    context = {
        'success': True,
    }
    return render(request, 'email.html', context)


def about(request):
    return render(request, 'about.html')
