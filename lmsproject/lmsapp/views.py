from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Student,Login
from datetime import date
from django.contrib import messages
from adminapp.models import Program, Branch, Year
from . smssender import sendsms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        emailaddress=request.POST['emailaddress']
        address=request.POST['address']
        contactno=request.POST['contactno']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate,contactno=contactno)
        enq.save()
        sendsms(contactno)
        messages.success(request,'Your Enquiry is submitted')
    return render(request,"contactus.html")
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        usertype=request.POST['usertype']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=="student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.success(request,'Invalid user')
    return render(request,"login.html")
    
def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        program=request.POST['program']
        branch=request.POST['branch']
        contactno=request.POST['contactno']
        password=request.POST['password']
        address=request.POST['address']
        emailaddress=request.POST['emailaddress']
        year=request.POST['year']
        regdate=date.today
        usertype='student'
        status='false'
        stu=Student(rollno=rollno, name=name, fname=fname, mname=mname, gender=gender, program=program, branch=branch, contactno=contactno, year=year, emailaddress=emailaddress, regdate=regdate,address=address)
        log=Login(userid=rollno, password=password,usertype=usertype, status=status)
        stu.save()
        log.save()
        subject='Important mail from Tilka Manghi Bhagalpur University'
        msg=f'Hello {name} Your Registration is Successfull and Your Password is{password}'
        # email_from=settings.EMAIL_HOST_USER
        # send_mail(subject,msg,email_from,[emailaddress]) 
        messages.success(request,'Student Registration done.')
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    return render(request,"registration.html",locals())
