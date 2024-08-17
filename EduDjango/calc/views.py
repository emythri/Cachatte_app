from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':"Raju"})

def dashboard(request):
    return render(request,'dashboard.html')

def career_test(request):
    return render(request,'career_test.html')

def add(request): 
    val1=int(request.POST['num1']) 
    val2=int(request.POST['num2']) 
    val3=val1+val2 
    return render(request,'result.html',{'result':val3}) 

def strudentView(request):
    cs_no = Students.objects.filter(course='Computer Science').count()
    cs_no= int(cs_no) 
    print('Number of Computer Science Students Are',cs_no)
    
    ce_no= Students.objects.filter(course='Computer Engineering').count()
    ce_no= int(ce_no)
    print('Number of Computer Engineering Students Are',ce_no)
    
    se_no= Students.objects.filter(course= 'Software Engineering').count() 
    se_no= int(se_no)
    print('Number of Software Engineering Students Are', se_no)
    
    sec_no =Students.objects.filter(course='Computer Security').count()
    sec_no= int(sec_no)
    print('Number of Computer Security Students Are', sec_no)
    
    male_no = Students.objects.filter(gender='Male').count() 
    male_no = int(male_no)
    print('Number of Male Are', male_no)
    
    female_no = Students.objects.filter(gender= 'Female').count()
    female_no= int(female_no)
    print('Number of Female Are', female_no)
    
    gender_list = ['Male','Female']
    gender_number = [male_no,female_no]
    
    course_list = ['Computer Science', 'Computer Engineering','Software Engineering','Computer Security']
    number_list = [cs_no,ce_no,se_no,sec_no]
    context = {'course_list':course_list,'number list':number_list,'gender list':gender_list,'gender_number':gender_number}
    return render(request,'career_test.html',context)
    