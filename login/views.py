from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from exam import settings
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .models import *
from . tokens import generate_token
import re
import numpy as np
from girth import ability_map
import io
import math as m
regex = r'[a-z]+\.\d{3}bct\d{3}@acem\.edu\.np'

questions_asked = []
responses = []
diss = []
diff =[]
cid = '1'
phy_count = 0
cheb_count = 0
che_count = 0
matb_count = 0
mat_count = 0
engb_count = 0
eng_count = 0
score = 0
score_phy = 0
score_chem = 0
score_math = 0
score_eng = 0
sub_value = 1
questions_finished = False
base = 0
sub_value_score = 1
qta = 5
# Create your views here.
def home(request):
    return render(request,"login/index.html")

def signup(request):

    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        dob =request.POST['dob']
        pass1 = request.POST['pass1']
        pass2 =request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,'Username Already Exists! Please try other Usernames')
            return redirect('signup')
        if re.fullmatch(regex,email) == None:
               messages.info(request,"Only ACEM bct students are accepted.")
               return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request,'Email already Registerd!')
            return redirect('signup')

        if len(username)>20:
            messages.error(request,'Username Must be under 15 Chaaracters')
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,"Password Didn't Match") 
            return redirect('signup')


        if not username.isalnum():
            messages.error(request,'Username Must Be Alpha-Numeric')
            return redirect('signup')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.middle_name =mname
        myuser.last_name =lname
        myuser.date_of_birth =dob 
        myuser.is_active =False
        myuser.save()

        messages.success(request,"Your Account Has Been Successfully Created. We have Sent you a Confirmation Email,Please Confirm your email in order to activate your account")

        

        #Email  Address Confirmation Email
        current_site=get_current_site(request)
        email_subject = "Confirm  your email @ Assesment Evaluation System Login!!"
        message2 = render_to_string('email_confirmation.html',{
            'name':myuser.first_name,
            'domain': current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser)
            
        })
        email =EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently=True
        email.send()

        #Welcome Email
        subject="Welcome To Assesment Evaluation System- Admin"
        message ="Hello"+ myuser.first_name+"!!\n"+"Welcome To Assesment Evaluation System Website\n We have sent you a confirmation email,please confirm your Email adddress in order to activate your Account.\n\n Thanking You"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True )
        

        return redirect('signin')
    return render(request,"login/signup.html")

def signin(request):
    global UserID
    if request.method=='POST':
        username = request.POST['username']
        pass1 =request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname= user.first_name
            UserID = username
            return render (request,"login/index.html",{'fname':fname})


        else:
            messages.error(request,"Bad Credentials")
            return redirect('signin')
    return render(request,"login/signin.html")



def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active =True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation-failed.html')


def signinas(request):
    return render(request,'login/signinas.html')

def about(request):
    return render(request,'login/about.html')

def clear_all():
    global cid 
    global phy_count 
    global cheb_count 
    global che_count 
    global matb_count
    global mat_count 
    global engb_count
    global eng_count 
    global score 
    global score_phy 
    global score_chem
    global score_math
    global score_eng 
    global sub_value 
    global questions_finished
    global base
    global sub_value_score
    global UserID
    cid = '1'
    phy_count = 0
    cheb_count = 0
    che_count = 0
    matb_count = 0
    mat_count = 0
    engb_count = 0
    eng_count = 0
    score = 0
    score_phy = 0
    score_chem = 0
    score_math = 0
    score_eng = 0
    sub_value = 1
    questions_finished = False
    base = 0
    sub_value_score = 1
    questions_asked.clear()
    responses.clear()
    diss.clear()
    diff.clear()    

def signout(request):
   logout(request)
   clear_all()
   messages.success(request,"Logged out Successfully!")
   return redirect('home')

def reset_values():
    
    questions_asked.clear()
    responses.clear()
    diss.clear()
    diff.clear()


def basequestion(request):
    global cid 
    global phy_count 
    global cheb_count 
    global che_count 
    global matb_count
    global mat_count 
    global engb_count
    global eng_count 
    global score 
    global score_phy 
    global score_chem
    global score_math
    global score_eng 
    global sub_value 
    global questions_finished
    global base
    global sub_value_score
    global UserID
    global qta
    if request.method == 'POST':

        if phy_count < qta:
            loop_var = int(request.POST.get('loop_var'))
            if loop_var == 0:
                sub_value = 1
                base = 1
                questions = basephyQuesModel.objects.all()
            elif loop_var == 1:
                questions = phyQuesModel.objects.filter(qid = cid)
                print(f'Your question: {questions}')
                phy_count = phy_count + 1
                if phy_count == qta:
                    sub_value=2
                    base = 0
        elif cheb_count == 0:
            reset_values()
            sub_value_score = 2
            questions = basechemQuesModel.objects.all()
            cheb_count += 1
            base = 1
        elif che_count < qta:
            questions = chemQuesModel.objects.filter(qid = cid)
            che_count += 1
            if che_count ==qta:
                sub_value = 3
                base = 0
        elif  matb_count == 0:
            reset_values()
            sub_value_score = 3
            questions = basemathQuesModel.objects.all()
            matb_count += 1
            base = 1
        elif matb_count == 1 and mat_count < qta:
            questions = mathQuesModel.objects.filter(qid = cid)
            mat_count +=1
            if mat_count == qta:
                sub_value = 4
                base = 0
        elif mat_count == qta and engb_count == 0:
            sub_value_score = 4
            reset_values()
            questions = baseengQuesModel.objects.all()
            engb_count += 1
            base = 1
        elif engb_count == 1 and eng_count < qta:
            questions = engQuesModel.objects.filter(qid = cid)
            eng_count += 1
            if eng_count == qta:
                questions_finished = True
        
        for q in questions:
            question = request.POST.get(q.question)
            print(f'QuestionChecked{question}')
            answer = q.ans
            if answer == question:
                new_response = [1]
                diss.append(q.dis)
                diff.append(q.dif)
                responses.append(new_response)
                if(sub_value_score == 1):
                    score_phy += 1
                    score += 1
                elif sub_value_score ==2:
                    score_chem += 1
                    score += 1
                elif sub_value_score == 3:
                    score_math += 1
                    score += 1
                elif sub_value_score == 4:
                    score_eng += 1
                    score += 1
            else:
                new_response = [0]
                diss.append(q.dis)
                diff.append(q.dif)
                responses.append(new_response)
        if questions_finished == False and base!=0:                
            response = np.array(responses).astype('int')
            print(f'response: {responses}')
            dis = np.array(diss)
            dif = np.array(diff)
            print(response)
            ability = ability_map(response,dif,dis)

            questionawa,prob = new_question(ability)


            context = {
            'questions':questionawa,
            'probability':round(prob,4)*100
                }
            return render(request,'login/question.html',context)
        elif base == 0:
            if sub_value == 2:
                questions = basechemQuesModel.objects.all()
            elif sub_value == 3:
                questions = basemathQuesModel.objects.all()
            elif sub_value == 4:
                questions = baseengQuesModel.objects.all()
            context ={
                'questions':questions
            }
            return render(request,'login/basequestion.html',context)

        elif questions_finished == True:
            p = Performance(USERID = UserID,Physics = score_phy,Chemistry = score_chem,Maths = score_math,English = score_eng,Total = score)
            p.save(force_insert = True)
            context={
                'phy_score':score_phy,
                'chem_score':score_chem,
                'math_score':score_math,
                'eng_score':score_eng,
                'total_score':score
            }
            return render(request,'login/result.html',context)

    else:
        questions = basephyQuesModel.objects.all()
        context = {
            'questions':questions
        }
        print('basequestion')
        print(context)
        return render(request,'login/basequestion.html',context)        

#function to calculate probability
def prob(abi,dif,dis):
    p = 1/(1+m.exp(-dis * (abi - dif)))
    return p

def new_question(ability):
    global cid
    global sub_value
    Pr=0
    Prob = []
    if sub_value == 1:
        questions=phyQuesModel.objects.all()
    elif sub_value == 2:
        questions=chemQuesModel.objects.all()
    elif sub_value == 3:
        questions=mathQuesModel.objects.all()
    elif sub_value == 4:
        questions=engQuesModel.objects.all()
    i=1
    Prob.append(0)
    qiqdd = '1'
    for q in questions:
        if q.qid not in  questions_asked:
            dis = float(q.dis)
            dif = float(q.dif)
            print(f'ab{ability}')
            Prob.append(prob(ability,dif,dis))
            if (Prob[i])>(Prob[i-1]):
                Pr = Prob[i]
                qiqdd = q.qid
            i+=1
    if sub_value == 1:
        question_to_ask = phyQuesModel.objects.filter(qid=qiqdd)
    if sub_value == 2:
        question_to_ask = chemQuesModel.objects.filter(qid=qiqdd)
    if sub_value == 3:
        question_to_ask = mathQuesModel.objects.filter(qid=qiqdd)
    if sub_value == 4:
        question_to_ask = engQuesModel.objects.filter(qid=qiqdd)
    questions_asked.append(qiqdd)
    cid = qiqdd
    print(f'question_to_ask: {question_to_ask}')
    print(f'Questions Asked{questions_asked}')
    return (question_to_ask,Pr)

def takeexam(request):
    if request.method=="POST":
        return render(request,'login/takeexam.html')

def performance(request):
    global UserID
    if User.is_staff == True:
        PerformanceDetails = Performance.objects.all()
    else:
        PerformanceDetails = Performance.objects.filter(USERID = UserID)
    context={
        'performance':PerformanceDetails
    }
    return render(request,'login/performance.html',context)

    