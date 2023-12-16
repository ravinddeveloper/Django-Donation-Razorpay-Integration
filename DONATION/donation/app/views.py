from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import donation

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def index(request):
    return render(request,'index.html')

def success(request):
    data=request.GET
    name=data.get('name')
    phone=data.get('phone')
    email=data.get('email')
    amount=data.get('amount')
    payment_id=data.get('payment_id')
    order = donation.objects.create(name=name,phone=phone,mail=email,amount=amount,payment_id=payment_id)

    html_msg=render_to_string('mail.html',{'name':name,'phone':phone,'amount':amount,'payment_id':payment_id,'email':email})
    message = strip_tags(html_msg)
    message=EmailMultiAlternatives(
        subject = 'Payment Received',
        body=message,
        from_email=None,
        to=[email]
    )
    message.attach_alternative(html_msg,'text/html')
    message.send()

    messages.info(request,"Payment success")
    return redirect('/')

def fail(request):
    messages.info(request,"Payment Failed")
    return redirect('/')



