from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import HomeContact
# signIn data
from .models import SignInUser
from django.contrib.auth import authenticate, login,logout,login

# Create your views here.

def index(request):
    return render(request,'index.html')

#  in home page contact us
def indexContact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        busines_email = request.POST.get('businessmail')
        userphno = request.POST.get('userphno')
        userjob = request.POST.get('userjob')
        userCompany = request.POST.get('userCompany')
        message = request.POST.get('message')
        
        if username:
            user_contact = HomeContact(
                username=username, 
                useremail=useremail, 
                busines_email=busines_email, 
                userphno=userphno, 
                userjob=userjob, 
                userCompany=userCompany, 
                message=message
            )
            user_contact.save()
            return redirect('success')
      
        else:
            error_msg = "Please provide a name."
            return HttpResponse(error_msg)

    else:
        error_msg = "Please fill all details."
        return render(request, 'success.html', {'message': error_msg})

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

def adminLogin(request):
    return render(request,'adminLogin.html')

def Aerospace(request):
    return render(request,'Aerospace&Defence.html')

def chatbot(request):
    return render(request,'AI-chatbot.html')

def angular(request):
    return render(request,'angular.html')



def automotive(request):
    return render(request,'automotive.html')

def aws(request):
    return render(request,'aws.html')

def azure(request):
    return render(request,'azure.html')

def Banking(request):
    return render(request,'Banking.html')

def bigdata(request):
    return render(request,'bigdata.html')



def capitalMarket(request):
    return render(request,'capital-market.html')



def Communications(request):
    return render(request,'Communications.html')

def ConsumerElectronics(request):
    return render(request,'Consumer-Electronics.html')

def consumerPackagedGoods(request):
    return render(request,'consumer-packaged-goods.html')

def cloud(request):
    return render(request,'cloud.html')

def Communications(request):
    return render(request,'Communications.html')

def ConsumerElectronics(request):
    return render(request,'Consumer-Electronics.html')

def contact(request):
    return render(request,'contact.html')

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

def EMS(request):
    return render(request,'EMS.html')

def EngineeringOperations(request):
    return render(request,'Engineering-Operations.html')

def financeManagement(request):
    return render(request,'finance-management.html')

def HealthCare(request):
    return render(request,'Health-care.html')

def hrManagement(request):
    return render(request,'hr-management.html')

def hrDashboard(request):
    return render(request,'hrDashboard.html')

def HMS(request):
    return render(request,'HMS.html')

def IndustrialProcess(request):
    return render(request,'Industrial-Process.html')

def insurance(request):
    return render(request,'insurance.html')

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



def marketDashboard(request):
    return render(request,'marketDashboard.html')

def media(request):
    return render(request,'media.html')

def MediaServices(request):
    return render(request,'Media&Services.html')

def mediaDashboard(request):
    return render(request,'mediaDashboard.html')

def NaturalResources(request):
    return render(request,'Natural-resources.html')

def NetworkProviders(request):
    return render(request,'Network-Edge-Providers.html')


def oilgas(request):
    return render(request,'oil&gas.html')




def php(request):
    return render(request,'php.html')

def SoftwareProducts(request):
    return render(request,'PlatformsSoftwareProducts.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def ProfessionalServices(request):
    return render(request,'Professional-Services.html')

def profileDashboard(request):
    return render(request,'profile-dashboard.html')

def PublicSector(request):
    return render(request,'Public-Sector.html')

def pythonPage(request):
    return render(request,'python-page.html')

def reactJs(request):
    return render(request,'reactJs.html')

def recruitmanagement(request):
    return render(request,'recruitmanagement.html')

def registrationForm(request):
    return render(request,'registration-form.html')

def Retail(request):
    return render(request,'Retail.html')

def salesforce(request):
    return render(request,'salesforce.html')

def sap(request):
    return render(request,'sap.html')

def securityNotifications(request):
    return render(request,'securityNotifications.html')

def Semiconductors(request):
    return render(request,'Semiconductors.html')

def solar(request):
    return render(request,'solar.html')

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
            student = SignInUser(user_name=user_name,user_email=user_email,password=password,re_password=re_password)
            student.save()
            return render(request,'student-login.html',{'message':'user created'})
        else:
            return render(request,'student-login.html',{'message':"Password not matching"})
    

# login student
def loginStudent(request):

    if request.method == 'POST':
        userName = request.POST['userName']
        login_password = request.POST['login_password']
        user = authenticate(request, userName=userName, login_password=login_password)
        if user is not None:
            return render(request, 'student-dashboard.html', {'userName': userName, 'user_student': user})
        else:
            return render(request, 'student-login.html', {'message': 'Invalid username or password'})
    else:
        return render(request, 'student-dashboard.html')

# logout function
def logOut_student(request):
    return render(request, 'student-login.html')




def TermsUse(request):
    return render(request,'Terms-of-use.html')

def thermal(request):
    return render(request,'thermal.html')

def trainerDashboard(request):
    return render(request,'trainerDashboard.html')

def TransportationServices(request):
    return render(request,'TransportationServices.html')

# fetching data in JSON formate

def TSARITdashboard(request):

    homePage = HomeContact.objects.all()

    web = ContactMessage.objects.filter(form_name = 'web-service').order_by('id')
    app = ContactMessage.objects.filter(form_name = 'app-service').order_by('id')
    bpo = ContactMessage.objects.filter(form_name = 'BPO-service').order_by('id')
    sateliteServ = ContactMessage.objects.filter(form_name = 'satelite-service').order_by('id')
    civil = ContactMessage.objects.filter(form_name = 'civil-service').order_by('id')

    all_Services = list(web) + list(app) + list(bpo) + list(sateliteServ) + list(civil)
    return render(request,'TSARIT-dashboard.html',{'allServices':all_Services,"homePage":homePage})

def Utilities(request):
    return render(request,'Utilities.html')


    
def wind(request):
    return render(request,'wind.html')


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

# service data

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

        form_name = 'man-power-service'
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

# Photo & Video Editing-------------------------------------------------------------------------

def photo_edting(request):
    return render(request,'photo-video-edting.html')

def PhotoVideoService(request):

    if request.method == 'POST':

        form_name = 'photoVideo-service'
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