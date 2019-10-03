from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import TaskInquiryForm, WebAppInquiryForm
import afterhours.settings as settings

# Create your views here.

def landing(request):
    return render(request,'inquiry/landing.html')

def taskinquiry(request):
    if request.method == 'GET':
        form = TaskInquiryForm()
        return render(request, 'inquiry/taskinquiry.html', {'form': form})
        # form = InquiryForm()
    else:
        form = TaskInquiryForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            email = form.cleaned_data['email']
            duration = form.cleaned_data['duration']
            try:
                #TODO impliment sending email here, probably build instance of EmailMessage
                send_mail(task, task + duration + 'My email is: ' + email, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                #TODO return error here if header is bad
             return redirect('failure')

    return render(request,'inquiry/success.html')

def webappinquiry(request):
    if request.method == 'GET':
        form = WebAppInquiryForm()
        return render(request, 'inquiry/webappinquiry.html', {'form': form})
        # form = InquiryForm()
    else:
        form = WebAppInquiryForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            email = form.cleaned_data['email']
            try:
                #TODO impliment sending email here, probably build instance of EmailMessage
                send_mail('Web App Request', app + ' My email is: ' + email, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                #TODO return error here if header is bad
             return redirect('failure')

    return render(request,'inquiry/success.html')

def success(request):
    return render(request, 'inquiry/success.html')

def failure(request):
    return render(request, 'inquiry/failure.html')
