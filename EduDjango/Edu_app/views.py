from django.shortcuts import render,redirect
from .models import *
from .models import Stream
#from .forms import StreamForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request,'home.html',{'name':"Raju"})

def dashboard(request):
    return render(request,'dashboard.html')

def career_test(request):
    return render(request,'career_test.html')

# def dashboard(request):
#     Students=Student.objects.all()
#     return render(request,'dashboard.html',{'users':users})

def stream(request):
    streams=Stream.objects.all()
    firstname=str(request.POST['n1'])
    lastname=str(request.POST['n2'])
    return render(request,'stream.html',{'first':firstname,'last':lastname,'streams':streams})

def navstream(request):
    streams=Stream.objects.all()
    return render(request,'navstream.html',{'streams':streams})



def subjects(request, stream_id):
    stream = Stream.objects.get(id=stream_id)
    subjects = stream.subjects.all()  # Assuming a relationship exists
    return render(request, 'subjects.html', {'stream': stream, 'subjects': subjects})


# def students_view(request):
#     return render(request, 'students_view.html')


def user_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user_profiles.html', {'profiles': profiles})

# def user_profile_view(request):
#     user = request.user  # Get the currently logged-in user
#     return render(request, 'user_profile.html', {'user': user})


 


# def subjects(request):
#     subjects=Subject.objects.all()
#     return render(request,'subjects.html',{'subjects':subjects})

# def users(request):
#     users=User.objects.all()
#     return render(request,'users.html',{'users':users})
    
# def create_stream(request):
#     if request.method == 'POST':
#         form = StreamForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('stream_list')
#     else:
#         form = StreamForm()
#     return render(request, 'create_stream.html', {'form': form})

# def stream_list(request):
#     streams = Stream.objects.all()
#     return render(request, 'stream_list.html', {'streams': streams})