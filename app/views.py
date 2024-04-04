from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import HomeContact
# signIn data
from .models import SignInUser
from django.contrib.auth.models import auth

# Create your views here.

def index(request):
    return render(request,'index.html')

#  in home page contact us
def indexContact(request):
    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        busines_email = request.POST['businessmail']
        userphno = request.POST['userphno']
        userjob = request.POST['userjob']
        userCompany = request.POST['userCompany']
        message = request.POST['message']
        
        if username:
            user_contact = HomeContact(username=username, useremail=useremail, busines_email=busines_email, userphno=userphno, userjob=userjob, userCompany=userCompany, message=message)
            user_contact.save()
            return redirect('success')
      
        else:
            error_msg = "Please provide a name."
            return HttpResponse(error_msg)

    else:
        error_msg = "Please fill all details."
        return render(request, 'success.html', {'message': error_msg})
    
def contact(request):
    return render(request,'contact.html')

from .models import ContactUs

def conactForm(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        usersubject = request.POST['subject']
        message = request.POST['message']
        conactusform = ContactUs.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            usersubject=usersubject,
            phone=phone,
            message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'conact.html')
    

def success_view(request):
    return render(request, 'success.html')

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

#  96

def about(request):
    return render(request,'about.html')

def accessbility(request):
    return render(request,'accessability.html')

def accountsDashboard(request):
    return render(request,'accounts-dashboard.html')


def Aerospace(request):
    return render(request,'Aerospace&Defence.html')

from .models import Industries

def aeroIndustry(request):
    if request.method == 'POST':

        form_name = 'Aerospace-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        userSatelite = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        userSatelite.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def angular(request):
    return render(request,'angular.html')



def automotive(request):
    return render(request,'automotive.html')

def automotivendustry(request):
    if request.method == 'POST':

        form_name = 'autoMotive-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        autoMotiveInd = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        autoMotiveInd.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def aws(request):
    return render(request,'aws.html')

def azure(request):
    return render(request,'azure.html')

def Banking(request):
    return render(request,'Banking.html')

def bankIndustry(request):
    if request.method == 'POST':

        form_name = 'banking-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        bankInd = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        bankInd.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')



def bigdata(request):
    return render(request,'bigdata.html')



def capitalMarket(request):
    return render(request,'capital-market.html')

def capitalIndustry(request):
    if request.method == 'POST':

        form_name = 'capitalMarket-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        capitalInd = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        capitalInd.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')



def Communications(request):
    return render(request,'Communications.html')

def communicationsIndustry(request):
    if request.method == 'POST':

        form_name = 'Communications-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        capitalInd = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        capitalInd.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def ConsumerElectronics(request):
    return render(request,'Consumer-Electronics.html')

def consumerIndustry(request):
    if request.method == 'POST':

        form_name = 'ConsumerElectronics-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        consumerInd = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        consumerInd.save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def consumerPackagedGoods(request):
    return render(request,'consumer-packaged-goods.html')

def cPackagedIndustry(request):
    if request.method == 'POST':

        form_name = 'consumerPackagedGoods-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        packagedGoods = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        packagedGoods .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def cloud(request):
    return render(request,'cloud.html')

def Communications(request):
    return render(request,'Communications.html')

def ConsumerElectronics(request):
    return render(request,'Consumer-Electronics.html')


def coockiesPolicy(request):
    return render(request,'coockies-policy.html')

def CorporateLogin(request):
    return render(request,'Corporate-login.html')

def csr(request):
    return render(request,'csr.html')

def dataScience(request):
    return render(request,'data-science.html')



def dotnet(request):
    return render(request,'dot-net.html')

def Education(request):
    return render(request,'Education.html')


def educationIndustry(request):
    if request.method == 'POST':

        form_name = 'Education-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        educIndus = Industries.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        educIndus .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')



def EngineeringOperations(request):
    return render(request,'Engineering-Operations.html')

def eng_operationIndustry(request):
    if request.method == 'POST':

        form_name = 'EngineeringOperations-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        healthInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        healthInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')




def HealthCare(request):
    return render(request,'Health-care.html')

def healthCareIndustry(request):
    if request.method == 'POST':

        form_name = 'healthCare-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        healthInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        healthInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def hrDashboard(request):
    return render(request,'hrDashboard.html')



def IndustrialProcess(request):
    return render(request,'Industrial-Process.html')

def industrialProcInd(request):
    if request.method == 'POST':

        form_name = 'IndustrialProcess-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        indProcInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        indProcInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def insurance(request):
    return render(request,'insurance.html')

def insuranceIndustry(request):
    if request.method == 'POST':

        form_name = 'insurance-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        insuranceInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        insuranceInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def internshipPage(request):
    return render(request,'internship-page.html')

def ItPromotions(request):
    return render(request,'It-promotions.html')

def Java(request):
    return render(request,'Java.html')

def jobApply(request):
    return render(request,'job-apply.html')

def jobPage(request):
    return render(request,'job-page.html')

def LifePharma(request):
    return render(request,'Life-Pharma.html')

def pharmaIndustry(request):
    if request.method == 'POST':

        form_name = 'LifePharma-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        pharmaInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        pharmaInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def marketDashboard(request):
    return render(request,'marketDashboard.html')

def media(request):
    return render(request,'media.html')

def MediaServices(request):
    return render(request,'Media&Services.html')

def mediaIndustry(request):
    if request.method == 'POST':

        form_name = 'MediaServices-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        mediaInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        )
        mediaInd .save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def mediaDashboard(request):
    return render(request,'mediaDashboard.html')

def NaturalResources(request):
    return render(request,'Natural-resources.html')

def naturalResIndustry(request):
    if request.method == 'POST':

        form_name = 'NaturalResources-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        natural = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def NetworkProviders(request):
    return render(request,'Network-Edge-Providers.html')

def networkIndustry(request):
    if request.method == 'POST':

        form_name = 'NetworkEdgeProviders-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        network = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def oilGas(request):
    return render(request,'oil&gas.html')

def oilGasIndustry(request):
    if request.method == 'POST':

        form_name = 'oilGas-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        oil = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')



def php(request):
    return render(request,'php.html')

def SoftwareProducts(request):
    return render(request,'PlatformsSoftwareProducts.html')

def softwareProductsIndustry(request):
    if request.method == 'POST':

        form_name = 'SoftwareProducts-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        software = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def ProfessionalServices(request):
    return render(request,'Professional-Services.html')

def serviceIndustry(request):
    if request.method == 'POST':

        form_name = 'ProfessionalServices-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        service = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def profileDashboard(request):
    return render(request,'profile-dashboard.html')

def PublicSector(request):
    return render(request,'Public-Sector.html')

def publicSectorIndustry(request):
    if request.method == 'POST':

        form_name = 'PublicSector-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        sector = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

def pythonPage(request):
    return render(request,'python-page.html')

def reactJs(request):
    return render(request,'reactJs.html')



def registrationForm(request):
    languages = [
    "select",
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "Go",
    "Rust",
    "TypeScript",
    "Dart",
    "R",
    "MATLAB",
    "Scala",
    "Perl",
    "Lua",
    "HTML",
    "CSS",
    "SQL",
    "Bash"
]
    return render(request,'registration-form.html',{"languages":languages})

def Retail(request):
    return render(request,'Retail.html')

def retailIndustry(request):
    if request.method == 'POST':

        form_name = 'Retail-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        retialInd = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')


def salesforce(request):
    return render(request,'salesforce.html')

def sap(request):
    return render(request,'sap.html')

def securityNotifications(request):
    return render(request,'securityNotifications.html')

def Semiconductors(request):
    return render(request,'Semiconductors.html')

def semiConductorsIndustry(request):
    if request.method == 'POST':

        form_name = 'Semiconductors-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        semiCndtrs = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')



def studentDashboard(request):
    return render(request,'student-dashboard.html')

def studentLogin(request):
    return render(request,'student-login.html')

# student sign in
def signInStudent(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        password = request.POST['password']
        re_password = request.POST.get('re_password')
        if re_password == password:
            student = SignInUser.objects.create(user_name=user_name,user_email=user_email,password=password,re_password=re_password)
            student.save()
            return render(request,'student-login.html',{'message':'user created'})
        else:
            return render(request,'student-login.html',{'message':"Password not matching"})
    

# login student
def loginStudent(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(user_name=user_name, password=password)
        if user is not None:
            return render(request, 'student-dashboard.html', {'userName': user_name, 'user_student': user})
        else:
            return render(request, 'student-login.html', {'message': 'Invalid username or password'})
    else:
        return render(request, 'student-dashboard.html')

# logout function
def logOut_student(request):
    return render(request, 'student-login.html')




def TermsUse(request):
    return render(request,'Terms-of-use.html')

def trainerDashboard(request):
    return render(request,'trainerDashboard.html')

def TransportationServices(request):
    return render(request,'TransportationServices.html')

def transportIndustry(request):
    if request.method == 'POST':

        form_name = 'TransportationServices-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        transport = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

# fetching data in JSON formate

# from django.http import JsonResponse
# from django.core.serializers import serialize



    # Return the serialized data as JSON response
    # return JsonResponse(all_Services, safe=False)

def Utilities(request):
    return render(request,'Utilities.html')

def utilitiesIndustry(request):
    if request.method == 'POST':

        form_name = 'Utilities-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        utility = Industries.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'Aerospace&Defence.html')

    
def LifteAtTSARIT(request):
    return render(request,'lifeAtTSARIT.html')
# services----------------------------------------------------------------------

from .models import ContactMessage

# Web Development-------------------------------------
def webDevelopment(request):
    return render(request,'web-development.html')

def serviceWebDev(request):

    if request.method == 'POST':

        form_name = 'web-service'
        first_name = request.POST['web_username']
        last_name = request.POST['web_lastName']
        email = request.POST['web_email']
        phone = request.POST['web_phone']
        jobTitle = request.POST['web_jobTitle']
        select = request.POST['web_select']
        company = request.POST['web_company']
        message = request.POST['web_message']
        webService = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        webService.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# App Development

def appDevelopment(request):
    return render(request,'app-development.html')

# app service data

def AppDevService(request):
    if request.method == 'POST':

        form_name = 'app-service'
        first_name = request.POST['app_userFirstName']
        last_name = request.POST['last_name']
        email = request.POST['emailId']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        appService = ContactMessage.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        appService.save()
        return redirect('success')
    
    return render(request, 'app-development.html')

# Bpo Projects ------------------------------------------------------------------------------

def BPOservices(request):
    return render(request,'BPO-services.html')

def ServiceBPO(request):
    if request.method == 'POST':
        form_name = 'BPO-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']

        bpoServ = ContactMessage(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        bpoServ.save()
        return redirect('success')
    return render(request, 'BPO-services.html')
# Background Verifications

# Satellite Projects-------------------------------------------------------------------------

def satelite(request):
    return render(request,'satelite.html')


def sateliteServices(request):
    if request.method == 'POST':

        form_name = 'satelite-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        userSatelite = ContactMessage.objects.create(
            form_name=form_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            jobTitle=jobTitle,
            select=select,
            company=company,
            message=message,
        )
        userSatelite.save()
        return redirect('success')
    return render(request, 'satelite.html')

# Civil Construction-------------------------------------------------------------------------

def civilConstructions(request):
    return render(request,'civil-constructions.html')

def civilService(request):

    if request.method == 'POST':

        form_name = 'civil-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        civilService = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        civilService.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Manpower Supply-------------------------------------------------------------------------

def manPowerSupply(request):
    return render(request,'man-power-supply.html')

def ManPowerService(request):

    if request.method == 'POST':

        form_name = 'man-power-supply-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        manPower = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        manPower.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Payroll-Jobs-------------------------------------------------------------------------

def PayrollJobs(request):
    return render(request,'Payroll-Jobs.html')

def payRollServ(request):

    if request.method == 'POST':

        form_name = 'payRoll-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        payROllservices = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        payROllservices.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Ngo Consultancy-------------------------------------------------------------------------


def NGO(request):
    return render(request,'NGO.html')

def NGOservice(request):

    if request.method == 'POST':

        form_name = 'NGO-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        ngoObj = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        ngoObj.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Photo & Video Editing-------------------------------------------------------------------------

def photo_edting(request):
    return render(request,'photo-video-edting.html')

def PhotoVideoService(request):

    if request.method == 'POST':

        form_name = 'photo&Video-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        photoAndVideo = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        photoAndVideo.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')
# Digital Marketing-------------------------------------------------------------------------


def digitalmarketing(request):
    return render(request,'digitalmarketing.html')

def DigitalMarketingServ(request):

    if request.method == 'POST':

        form_name = 'digital-Marketing-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        dmMarketing = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        dmMarketing.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Survey-------------------------------------------------------------------------

def Survey(request):
    return render(request,'Survey.html')

def SurveyService(request):

    if request.method == 'POST':

        form_name = 'survey-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        surveyServ = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        surveyServ.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')

# Distribution-------------------------------------------------------------------------


def distribution(request):
    return render(request,'distribution.html')

def distributionService(request):

    if request.method == 'POST':

        form_name = 'distribution-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
        company = request.POST['company']
        message = request.POST['message']
        distribute = ContactMessage.objects.create(form_name=form_name,first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    phone=phone,
                                    jobTitle=jobTitle,
                                    select=select,
                                    company=company,
                                    message=message)
        distribute.save()
        return render(request, 'success.html',{'username':first_name})
    else:
        return render(request,'web-development.html')
    

    # energy services
from .models import Energy


def solar(request):
    return render(request,'solar.html')

def solaarEn(request):
    if request.method == 'POST':

        form_name = 'solar-energy'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        solaar = Energy.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'solar.html')

def wind(request):
    return render(request,'wind.html')

def windEnergy(request):
    if request.method == 'POST':

        form_name = 'Utilities-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        windEn = Energy.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'wind.html')

def thermal(request):
    return render(request,'thermal.html')

def thermalEnergy(request):
    if request.method == 'POST':

        form_name = 'Utilities-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        thermalEn = Energy.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')



# products
from .models import Products

def HMS(request):
    return render(request,'HMS.html')

def hospitalMS(request):
    if request.method == 'POST':

        form_name = 'Hospital Management System'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        hms = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')

def chatbot(request):
    return render(request,'AI-chatbot.html')

def AIchatBot(request):
    if request.method == 'POST':

        form_name = 'AI-Chatbot'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        ai = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')

def EMS(request):
    return render(request,'EMS.html')

def educationMS(request):
    if request.method == 'POST':

        form_name = 'Education Management System'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        thermalEn = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')

def financeManagement(request):
    return render(request,'finance-management.html')

def FMS(request):
    if request.method == 'POST':

        form_name = 'finance Management System'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        fms = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')

def recruitmanagement(request):
    return render(request,'recruitmanagement.html')

def RMS(request):
    if request.method == 'POST':

        form_name = 'Utilities-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        thermalEn = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')

def hrManagement(request):
    return render(request,'hr-management.html')

def HRM(request):
    if request.method == 'POST':

        form_name = 'Utilities-industry'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select_service']
        company = request.POST['company']
        message = request.POST['message']
        human = Products.objects.create(form_name=form_name,first_name=first_name,last_name=last_name,email=email,phone=phone,jobTitle=jobTitle,select=select,company=company,message=message,
        ).save()
    
        return render(request, 'success.html',{'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
    return render(request, 'thermal.html')
