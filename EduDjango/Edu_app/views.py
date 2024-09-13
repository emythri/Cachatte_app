from django.shortcuts import render,redirect
from .models import *
from .models import Stream
from .forms import StreamForm


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':"Raju"})

def dashboard(request):
    return render(request,'dashboard.html')

def career_test(request):
    return render(request,'career_test.html')

def dashboard(request):
    users=User.objects.all()
    return render(request,'dashboard.html',{'users':users})

def stream(request):
    streams=Stream.objects.all()
    firstname=str(request.POST['n1'])
    lastname=str(request.POST['n2'])
    return render(request,'stream.html',{'first':firstname,'last':lastname,'streams':streams})

def navstream(request):
    streams=Stream.objects.all()
    return render(request,'navstream.html',{'streams':streams})
    


def subjects(request):
    subjects=Subject.objects.all()
    return render(request,'subjects.html',{'subjects':subjects})

def users(request):
    users=User.objects.all()
    return render(request,'users.html',{'users':users})
    
def create_stream(request):
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
    else:
        form = StreamForm()
    return render(request, 'create_stream.html', {'form': form})

def stream_list(request):
    streams = Stream.objects.all()
    return render(request, 'stream_list.html', {'streams': streams})