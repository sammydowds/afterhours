from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request,'projects/yourprojects.html')

def yourprojects(request):
    return render(request, 'projects/yourprojects.html')
