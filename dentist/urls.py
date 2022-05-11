from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    # REGISTER & LOGIN URL PATHS
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),

    # APPOINTMENT URL PATHS
    path('book_appointment/', views.book_appointment, name="book_appointment"),
    # path('confirm_appointment/<str:pk>/', views.confirm_appointment, name="confirmappointment"),
    path('my_appointments/', views.my_appointments, name="my_appointments"),
    path('update_appointment/<str:pk>/', views.update_appointment, name="update_appointment"),
    path('delete_appointment/<str:pk>/', views.delete_appointment, name="delete_appointment"),


    # MAIN PATHS
    path('about.html/', views.about, name="about"),
    path('service.html/', views.service, name="service"),
    path('pricing.html/', views.pricing, name="pricing"),




    # CONTACTS AND EMAILING
    path('', views.home, name="home"),
    path('contact.html/', views.contact, name="contact"),
    path('email.html/', views.email, name="email"),


    # ADMIN-SERVICE ACCESS URL PATHS
    path('createservice.html/', views.create_service, name='createservice'),
    path('updateservice.html/<str:pk>/',
         views.update_service, name="updateservice"),
    path('deleteservice.html/<str:pk>/',
         views.delete_service, name="deleteservice"),




    # PASSWORD RESET URL PATHS
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_done.html"), name="password_reset_complete"),
]
