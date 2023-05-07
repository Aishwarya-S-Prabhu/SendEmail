from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings

def sendMail(request):
    number = 55  # Hardcoded value to check
    threshold = 50
    if number < threshold:
        send_mail(
        subject='Warning alert',
        message='Profit value is below set threshold value',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])
    return HttpResponse('Function complete.')
        
    
        
