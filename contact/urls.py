from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.ContactFormView.as_view(), name='contact_form'),
    path('submitted/', views.ContactFormView.as_view(), name='form_submitted'),
]