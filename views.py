from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app.models import Course,Student
from django.db.models import Q
from .forms import StudentRegistrationForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import StudentRegistrationForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.
def index(request):
    #return HttpResponse("Hello Avanti")
    #return HttpResponseRedirect('blogform')
    return redirect('home')

def name(request,name):
    content="<h1>Hello:{}</h1>".format(name)
    return HttpResponse(content)
    
   

def delete(request,x1,x2):
    
    content="x1 is:{}and x2:{}".format(x1,x2)
    return HttpResponse(content)

def postblog(request):
    return HttpResponse(form)

    form='''

             <html>
                <head>
                    <title>BLOG|Create</title>
                </head>
                <body>
                <form method="POST">
                <table>
                    <tr>
                      <td>Heading:</td>
                                                        
                      <td><input type="text" name="bhead"/></td>
                    </tr>

                    <tr>
                      <td>Category:</td>
                      <td><input type="text" name="bcat"/></td>
                    </tr>

                                                
                            
                    <tr>
                        <td>Description:</td>
                        <td><textarea name="bdes" cols="30" rows="10"></textarea></td>
                    </tr>
                    <tr>
                                                       
                        <td><input type="submit" name="send" value="POST"/></td>
                    </tr>
                </table>
                </form>
                </body>
        </html>

    '''
    return HttpResponse(form)

def home(request):


    #return HttpResponse('home.html')  it didn't render html

    #return render(request,"home.html",{'a':'apple'})  

    context={'a':'Through Context',
             'l':[10,20,30],
             't':(50,60,70),
             's':{1,3,4,5,6,7,8}
    
    }
    
    context={'x':120,'y':40,'z':100}
    return render(request,'home.html',context)


def contact(request):

    #return render(request,'contact.html')
    mn=request.POST['mn']
    fd=request.POST['feedback']
    content={'m':mn,'f':fd}
    return render(request,'contact.html',content)
    return  render(request,'contact.html')

def placement(request):
    return render(request,'placement.html')

def create(request):
    return render(request,'createblog.html')

def store(request):
    '''
    h=request.GET['bhead']
    c=request.GET['bcat']
    d=request.GET['bdes']
    '''
    h=request.POST['bhead']
    c=request.POST['bcat']
    d=request.POST['bdes']
    data=h+'-'+c+'-'+d
    return HttpResponse(data)

def getform(request):
    return render(request,"form.html")    


def courseform(request):
    return render(request,"create_course.html")


def create_course(request):
   if request.method=='POST':  
    x=request.POST['cname']
    y=request.POST['cdur']
    z=request.POST['cprice']
   if y=='':
     c1=Course.objects.create(cname=x,cprice=z)
   else:
     c1=Course.objects.create(cname=x,cdur=y,cprice=z)
   
   
   c1.save() #work insert query internally
    #return HttpResponse('Record inserted Successfully')
    #return HttpResponse(cname+cdur+cprice)
   return redirect('/')
   '''
  else:

    return HttpResponse("In else block")  
'''

def get_course(request):
    content={}
    #content['data']=Course.c_manager.order_by('-cprice').all()
    content['data']=Course.objects.all()
    #content['data']=Course.c_manager.sort_desc_price()
    return render(request,'dashboard.html',content)
    #return HttpResponse('In get_course')

def delete(request,rid):
    x=Course.objects.get(id=rid)
    x.delete()
    return redirect('/')
    #return HttpResponse("Id is: <h1>"+rid+"<h1>")

def edit(request,rid):
  
    if request.method=='POST':

        x=request.POST['cname']
        y=request.POST['cdur']
        z=request.POST['cprice']

        c=Course.objects.filter(id=rid)
        c.update(cname=x,cdur=y,cprice=z)
        return redirect('/')
        
    else:
        content={}
        content['data']=Course.objects.get(id=rid)
        return render(request,'edit.html',content)
        #return HttpResponse("Id is: <h1>"+rid+"<h1>")

def filter_records(request):
    content={}
    #content['data']=Course.objects.filter(cdur=40)
    #select * from where cdur=20
    #content['data']=Course.objects.filter(cprice__lt=20000)
    #content['data']=Course.objects.filter(cprice__gt=20000)
    #content['data']=Course.objects.filter(cprice__lte=20000)
    #content['data']=Course.objects.filter(cprice__lte=20000)
    '''
    q1=Q(cprice__gt=40)
    q2=Q(cprice__gt=20000)
    content['data']=Course.objects.filter(q1 & q2)
    '''
    #content['data']=Course.objects.filter(cdur__lt=40,cprice__lt=20000)
    '''
    q1=Q(cdur__gt=40)
    q2=Q(cprice__gt=20000)
    content['data']=Course.objects.filter(q1 | q2)#OR opearations
    '''
    #order_by
    #content['data']=Course.objects.order_by('cprice')#ascending
    #content['data']=Course.objects.order_by('-cprice')#descending
    #content['data']=Course.objects.order_by('cprice').filter(cprice__gt-20000)
    #exclude()
    #content['data']=Course.objects.exclude(cprice__lte=20000)
    #content['data']=Course.objects.exclude(cprice__gte=20000)
    return render(request,'dashboard.html',content)  


def showformdata(request):

    if request.method=="POST":
        fm=StudentRegistrationForm(request.POST)
        #print("in post section")
        #print(fm)
        if fm.is_valid():
            sname=fm.cleaned_data['name']
            semail=fm.cleaned_data['email']
            #print(sname)
            #print(semail)
            #s1=Student.objects.create(name=sname,email=semail)
            s1=Student(name=sname,email=semail)
            s1.save()
            '''
            print("Data has passed validation")
        else:
            print("Data is not validated")    
    '''
    else:
        fm=StudentRegistrationForm()
        #print("IN GET SECTION empty")
    return render(request,'dform.html',{'form':fm})


def register(request):

    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        #print(fm)
        if fm.is_valid():
            #uname=fm.cleaned_data['username']
            #password=fm.cleaned_data['password1']
            #print(uname)
            #print(password)
            #u1=User(username=uname,password=password)
            #u1.save()
            fm.save()
            return HttpResponseRedirect('login')
    else:
        #fm=UserCreationForm()
        fm=SignUpForm()
    
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if request.method=="POST":
        #pass
        fm=AuthenticationForm(request=request,data=request.POST)

        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return HttpResponseRedirect('profile')
            #print(u)
    else:
        fm=AuthenticationForm()
        #fm=SignUpForm()
        return render(request,'login.html',{'form':fm})


        
def user_profile(request):
    return render(request,'profile.html') 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')       


def set_cookie(request):

    res=render(request,'setcookie.html')
    res.set_cookie('name','ITVEDANT-ECLASS-DJANGO')
    return res

def get_cookie(request):

    #v=request.COOKIES['name'] 
    #v=request.COOKIES.get('name') #None
    v=request.COOKIES.get('name','Guest')
    return render(request,'getcookie.html',{'value':v})

def del_cookie(request):

    res=render(request,'delcookie.html')
    res.delete_cookie('name')
    return res      


def set_session(request):
    request.session['name']='ITVEDANT ECLASS DJANGO SESSION'
    return render(request,'setsession.html')   

def get_session(request):
    v=request.session['name']
    return render(request,'getsession.html',{'value':v})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'delsession.html')   


def home(request):
    print("I am in View")
    return HttpResponse("This is Home Page")              

       