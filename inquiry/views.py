from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request,'inquiry/landing.html')

def inquiry(request):
    if request.method == 'GET':
        form = InquiryForm()
    else:
        form = InquiryForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                #impliment sending email here, probably build instance of EmailMessage 
            except BadHeaderError:
                #return error here if header is bad
             return redirect('success')

    return render(request,'inquiry/inquiry.html')

def succes(request):
    return render(request, 'inquiry/landing.html')
