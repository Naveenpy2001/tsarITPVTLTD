from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import logout
from .models import HomeContact
# signIn data
from .models import SignInUser
from django.contrib.auth.models import auth

from .models import MediaPost
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
            user_contact = HomeContact.objects.create(username=username, useremail=useremail, busines_email=busines_email, userphno=userphno, userjob=userjob, userCompany=userCompany, message=message)
            user_contact.save()
            return render(request, 'success.html', {'message':'Request has been sent !',"name":username,'info':'our team will be contact you within 24:00 Hours.'})
        else:
            error_msg = "Please provide a name."
            return HttpResponse(error_msg)
    else:
        return render(request, 'success.html', {'message':'Request has been sent !',"name":username,'info':'our team will be contact you within 24:00 Hours.'})
    
# contactUs page
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



def Communications(request):
    return render(request,'Communications.html')

def ConsumerElectronics(request):
    return render(request,'Consumer-Electronics.html')


def coockiesPolicy(request):
    return render(request,'coockies-policy.html')



def csr(request):
    return render(request,'csr.html')



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



def ItPromotions(request):
    return render(request,'It-promotions.html')



# jobs page
from .models import Job

def jobPage(request):
    jobs = Job.objects.all()
    return render(request,'job-page.html',{'jobs':jobs})


from django.contrib.auth.models import User
from .models import JobApply

# CHATGPT

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Job, JobApply
from django.contrib import messages

def jobApply(request, job_id):
    if not request.session.get('email'):
        job = get_object_or_404(Job, pk=job_id)
        return render(request, 'job-apply.html',{'job':job})
    country_phone_codes = {

        "select": "country",
        "Afghanistan": "+93",
        "Albania": "+355",
        "Algeria": "+213",
        "Andorra": "+376",
        "Angola": "+244",
        "Antigua and Barbuda": "+1",
        "Argentina": "+54",
        "Armenia": "+374",
        "Australia": "+61",
        "Austria": "+43",
        "Azerbaijan": "+994",
        "Bahamas": "+1",
        "Bahrain": "+973",
        "Bangladesh": "+880",
        "Barbados": "+1",
        "Belarus": "+375",
        "Belgium": "+32",
        "Belize": "+501",
        "Benin": "+229",
        "Bhutan": "+975",
        "Bolivia": "+591",
        "Bosnia and Herzegovina": "+387",
        "Botswana": "+267",
        "Brazil": "+55",
        "Brunei": "+673",
        "Bulgaria": "+359",
        "Burkina Faso": "+226",
        "Burundi": "+257",
        "Cabo Verde": "+238",
        "Cambodia": "+855",
        "Cameroon": "+237",
        "Canada": "+1",
        "Central African Republic": "+236",
        "Chad": "+235",
        "Chile": "+56",
        "China": "+86",
        "Colombia": "+57",
        "Comoros": "+269",
        "Congo": "+242",
        "Costa Rica": "+506",
        "Croatia": "+385",
        "Cuba": "+53",
        "Cyprus": "+357",
        "Czech Republic": "+420",
        "Denmark": "+45",
        "Djibouti": "+253",
        "Dominica": "+1",
        "Dominican Republic": "+1",
        "East Timor (Timor-Leste)": "+670",
        "Ecuador": "+593",
        "Egypt": "+20",
        "El Salvador": "+503",
        "Equatorial Guinea": "+240",
        "Eritrea": "+291",
        "Estonia": "+372",
        "Eswatini": "+268",
        "Ethiopia": "+251",
        "Fiji": "+679",
        "Finland": "+358",
        "France": "+33",
        "Gabon": "+241",
        "Gambia": "+220",
        "Georgia": "+995",
        "Germany": "+49",
        "Ghana": "+233",
        "Greece": "+30",
        "Grenada": "+1",
        "Guatemala": "+502",
        "Guinea": "+224",
        "Guinea-Bissau": "+245",
        "Guyana": "+592",
        "Haiti": "+509",
        "Honduras": "+504",
        "Hungary": "+36",
        "Iceland": "+354",
        "India": "+91",
        "Indonesia": "+62",
        "Iran": "+98",
        "Iraq": "+964",
        "Ireland": "+353",
        "Israel": "+972",
        "Italy": "+39",
        "Jamaica": "+1",
        "Japan": "+81",
        "Jordan": "+962",
        "Kazakhstan": "+7",
        "Kenya": "+254",
        "Kiribati": "+686",
        "Korea, North": "+850",
        "Korea, South": "+82",
        "Kosovo": "+383",
        "Kuwait": "+965",
        "Kyrgyzstan": "+996",
        "Laos": "+856",
        "Latvia": "+371",
        "Lebanon": "+961",
        "Lesotho": "+266",
        "Liberia": "+231",
        "Libya": "+218",
        "Liechtenstein": "+423",
        "Lithuania": "+370",
        "Luxembourg": "+352",
        "Madagascar": "+261",
        "Malawi": "+265",
        "Malaysia": "+60",
        "Maldives": "+960",
        "Mali": "+223",
        "Malta": "+356",
        "Marshall Islands": "+692",
        "Mauritania": "+222",
        "Mauritius": "+230",
        "Mexico": "+52",
        "Micronesia": "+691",
        "Moldova": "+373",
        "Monaco": "+377",
        "Mongolia": "+976",
        "Montenegro": "+382",
        "Morocco": "+212",
        "Mozambique": "+258",
        "Myanmar (Burma)": "+95",
        "Namibia": "+264",
        "Nauru": "+674",
        "Nepal": "+977",
        "Netherlands": "+31",
        "New Zealand": "+64",
        "Nicaragua": "+505",
        "Niger": "+227",
        "Nigeria": "+234",
        "North Macedonia": "+389",
        "Norway": "+47",
        "Oman": "+968",
        "Pakistan": "+92",
        "Palau": "+680",
        "Palestine": "+970",
        "Panama": "+507",
        "Papua New Guinea": "+675",
        "Paraguay": "+595",
        "Peru": "+51",
        "Philippines": "+63",
        "Poland": "+48",
        "Portugal": "+351",
        "Qatar": "+974",
        "Romania": "+40",
        "Russia": "+7",
        "Rwanda": "+250",
        "Saint Kitts and Nevis": "+1",
        "Saint Lucia": "+1",
        "Saint Vincent and the Grenadines": "+1",
        "Samoa": "+685",
        "San Marino": "+378",
        "Sao Tome and Principe": "+239",
        "Saudi Arabia": "+966",
        "Senegal": "+221",
        "Serbia": "+381",
        "Seychelles": "+248",
        "Sierra Leone": "+232",
        "Singapore": "+65",
        "Slovakia": "+421",
        "Slovenia": "+386",
        "Solomon Islands": "+677",
        "Somalia": "+252",
        "South Africa": "+27",
        "South Sudan": "+211",
        "Spain": "+34",
        "Sri Lanka": "+94",
        "Sudan": "+249",
        "Suriname": "+597",
        "Sweden": "+46",
        "Switzerland": "+41",
        "Syria": "+963",
        "Taiwan": "+886",
        "Tajikistan": "+992",
        "Tanzania": "+255",
        "Thailand": "+66",
        "Togo": "+228",
        "Tonga": "+676",
        "Trinidad and Tobago": "+1",
        "Tunisia": "+216",
        "Turkey": "+90",
        "Turkmenistan": "+993",
        "Tuvalu": "+688",
        "Uganda": "+256",
        "Ukraine": "+380",
        "United Arab Emirates": "+971",
        "United Kingdom": "+44",
        "United States": "+1",
        "Uruguay": "+598",
        "Uzbekistan": "+998",
        "Vanuatu": "+678",
        "Vatican City": "+379",
        "Venezuela": "+58",
        "Vietnam": "+84",
        "Yemen": "+967",
        "Zambia": "+260",
        "Zimbabwe": "+263"
    }
    job = get_object_or_404(Job, pk=job_id)
    user = get_object_or_404(JobApply, email=request.session['email'])
    if request.method == 'POST':
        JobApply.objects.create(
            form_name=job.title,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            country_code=user.country_code,
            phone_number=user.phone_number,
            gender=user.gender,
            aadhar_card_number=user.aadhar_card_number,
            is_fresher=request.POST.get('is_fresher'),
            applied_with_tsar_it=request.POST.get('applied_with_tsar_it'),
            previous_employee_id=request.POST.get('previous_employee_id'),
            resume=request.FILES.get('resume'),
            terms_of_use_agreed=request.POST.get('terms_of_use_agreed'),
        ).save()
        job.applicants.add(user)
        return redirect('user_account')
    
    return render(request, 'job-apply.html', {'job': job, 'country_phone_codes': country_phone_codes})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = JobApply.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('user_account')
            else:
                messages.error(request, 'Incorrect password')
        except JobApply.DoesNotExist:
            messages.error(request, 'User does not exist')
    
    return render(request, 'login.html')

def user_account(request):
    if not request.session.get('email'):
        return redirect('login')

    user = get_object_or_404(JobApply, email=request.session['email'])
    applied_jobs = user.applied_jobs.all()
    return render(request, 'user_account.html', {'user': user, 'applied_jobs': applied_jobs})

def logoutUser(request):
    request.session.flush()
    return redirect('login')

# def jobApply(request, job_id):
#     country_phone_codes = {
#         "select": "country",
#         "Afghanistan": "+93",
#         "Albania": "+355",
#         "Algeria": "+213",
#         "Andorra": "+376",
#         "Angola": "+244",
#         "Antigua and Barbuda": "+1",
#         "Argentina": "+54",
#         "Armenia": "+374",
#         "Australia": "+61",
#         "Austria": "+43",
#         "Azerbaijan": "+994",
#         "Bahamas": "+1",
#         "Bahrain": "+973",
#         "Bangladesh": "+880",
#         "Barbados": "+1",
#         "Belarus": "+375",
#         "Belgium": "+32",
#         "Belize": "+501",
#         "Benin": "+229",
#         "Bhutan": "+975",
#         "Bolivia": "+591",
#         "Bosnia and Herzegovina": "+387",
#         "Botswana": "+267",
#         "Brazil": "+55",
#         "Brunei": "+673",
#         "Bulgaria": "+359",
#         "Burkina Faso": "+226",
#         "Burundi": "+257",
#         "Cabo Verde": "+238",
#         "Cambodia": "+855",
#         "Cameroon": "+237",
#         "Canada": "+1",
#         "Central African Republic": "+236",
#         "Chad": "+235",
#         "Chile": "+56",
#         "China": "+86",
#         "Colombia": "+57",
#         "Comoros": "+269",
#         "Congo": "+242",
#         "Costa Rica": "+506",
#         "Croatia": "+385",
#         "Cuba": "+53",
#         "Cyprus": "+357",
#         "Czech Republic": "+420",
#         "Denmark": "+45",
#         "Djibouti": "+253",
#         "Dominica": "+1",
#         "Dominican Republic": "+1",
#         "East Timor (Timor-Leste)": "+670",
#         "Ecuador": "+593",
#         "Egypt": "+20",
#         "El Salvador": "+503",
#         "Equatorial Guinea": "+240",
#         "Eritrea": "+291",
#         "Estonia": "+372",
#         "Eswatini": "+268",
#         "Ethiopia": "+251",
#         "Fiji": "+679",
#         "Finland": "+358",
#         "France": "+33",
#         "Gabon": "+241",
#         "Gambia": "+220",
#         "Georgia": "+995",
#         "Germany": "+49",
#         "Ghana": "+233",
#         "Greece": "+30",
#         "Grenada": "+1",
#         "Guatemala": "+502",
#         "Guinea": "+224",
#         "Guinea-Bissau": "+245",
#         "Guyana": "+592",
#         "Haiti": "+509",
#         "Honduras": "+504",
#         "Hungary": "+36",
#         "Iceland": "+354",
#         "India": "+91",
#         "Indonesia": "+62",
#         "Iran": "+98",
#         "Iraq": "+964",
#         "Ireland": "+353",
#         "Israel": "+972",
#         "Italy": "+39",
#         "Jamaica": "+1",
#         "Japan": "+81",
#         "Jordan": "+962",
#         "Kazakhstan": "+7",
#         "Kenya": "+254",
#         "Kiribati": "+686",
#         "Korea, North": "+850",
#         "Korea, South": "+82",
#         "Kosovo": "+383",
#         "Kuwait": "+965",
#         "Kyrgyzstan": "+996",
#         "Laos": "+856",
#         "Latvia": "+371",
#         "Lebanon": "+961",
#         "Lesotho": "+266",
#         "Liberia": "+231",
#         "Libya": "+218",
#         "Liechtenstein": "+423",
#         "Lithuania": "+370",
#         "Luxembourg": "+352",
#         "Madagascar": "+261",
#         "Malawi": "+265",
#         "Malaysia": "+60",
#         "Maldives": "+960",
#         "Mali": "+223",
#         "Malta": "+356",
#         "Marshall Islands": "+692",
#         "Mauritania": "+222",
#         "Mauritius": "+230",
#         "Mexico": "+52",
#         "Micronesia": "+691",
#         "Moldova": "+373",
#         "Monaco": "+377",
#         "Mongolia": "+976",
#         "Montenegro": "+382",
#         "Morocco": "+212",
#         "Mozambique": "+258",
#         "Myanmar (Burma)": "+95",
#         "Namibia": "+264",
#         "Nauru": "+674",
#         "Nepal": "+977",
#         "Netherlands": "+31",
#         "New Zealand": "+64",
#         "Nicaragua": "+505",
#         "Niger": "+227",
#         "Nigeria": "+234",
#         "North Macedonia": "+389",
#         "Norway": "+47",
#         "Oman": "+968",
#         "Pakistan": "+92",
#         "Palau": "+680",
#         "Palestine": "+970",
#         "Panama": "+507",
#         "Papua New Guinea": "+675",
#         "Paraguay": "+595",
#         "Peru": "+51",
#         "Philippines": "+63",
#         "Poland": "+48",
#         "Portugal": "+351",
#         "Qatar": "+974",
#         "Romania": "+40",
#         "Russia": "+7",
#         "Rwanda": "+250",
#         "Saint Kitts and Nevis": "+1",
#         "Saint Lucia": "+1",
#         "Saint Vincent and the Grenadines": "+1",
#         "Samoa": "+685",
#         "San Marino": "+378",
#         "Sao Tome and Principe": "+239",
#         "Saudi Arabia": "+966",
#         "Senegal": "+221",
#         "Serbia": "+381",
#         "Seychelles": "+248",
#         "Sierra Leone": "+232",
#         "Singapore": "+65",
#         "Slovakia": "+421",
#         "Slovenia": "+386",
#         "Solomon Islands": "+677",
#         "Somalia": "+252",
#         "South Africa": "+27",
#         "South Sudan": "+211",
#         "Spain": "+34",
#         "Sri Lanka": "+94",
#         "Sudan": "+249",
#         "Suriname": "+597",
#         "Sweden": "+46",
#         "Switzerland": "+41",
#         "Syria": "+963",
#         "Taiwan": "+886",
#         "Tajikistan": "+992",
#         "Tanzania": "+255",
#         "Thailand": "+66",
#         "Togo": "+228",
#         "Tonga": "+676",
#         "Trinidad and Tobago": "+1",
#         "Tunisia": "+216",
#         "Turkey": "+90",
#         "Turkmenistan": "+993",
#         "Tuvalu": "+688",
#         "Uganda": "+256",
#         "Ukraine": "+380",
#         "United Arab Emirates": "+971",
#         "United Kingdom": "+44",
#         "United States": "+1",
#         "Uruguay": "+598",
#         "Uzbekistan": "+998",
#         "Vanuatu": "+678",
#         "Vatican City": "+379",
#         "Venezuela": "+58",
#         "Vietnam": "+84",
#         "Yemen": "+967",
#         "Zambia": "+260",
#         "Zimbabwe": "+263"
#     }
#     job = get_object_or_404(Job, pk=job_id)
#     if request.method == 'POST':
#         form_name = job.title
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         country_code = request.POST.get('country_code')
#         phone_number = request.POST.get('phone_number')
#         gender = request.POST.get('gender')
#         aadhar_card_number = request.POST.get('aadhar_card_number')
#         is_fresher = request.POST.get('is_fresher')
#         applied_with_tsar_it = request.POST.get('applied_with_tsar_it')
#         previous_employee_id = request.POST.get('previous_employee_id')
#         resume = request.FILES.get('resume')
#         terms_of_use_agreed = request.POST.get('terms_of_use_agreed')
#         apply = JobApply.objects.create(form_name=form_name,email=email,password=password,first_name=first_name,last_name=last_name,country_code=country_code,phone_number=phone_number,gender=gender,aadhar_card_number=aadhar_card_number,is_fresher=is_fresher,applied_with_tsar_it=applied_with_tsar_it,previous_employee_id=previous_employee_id,resume=resume,terms_of_use_agreed=terms_of_use_agreed,)
#         apply.save()
#         jobs = get_object_or_404(Job, pk=job_id)
#         return render(request,'user_account.html',{'jobs':jobs,'first_name':first_name,'email':email})
#     return render(request,'job-apply.html',{'job':job,'country_phone_codes':country_phone_codes})

# from django.contrib.auth.hashers import make_password, check_password

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             student = JobApply.objects.get(email=email) 
#             if student.password == check_password.password:
#                 # You might want to add additional logic here such as setting session variables
#                 return render(request,'user_account.html') 
#             else:
#                 # Handle incorrect password
#                 pass
#         except JobApply.DoesNotExist:
#             # Handle non-existent user
#             pass
#     return render(request, 'job-apply.html')


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

def Media(request):
    posts = MediaPost.objects.all()
    return render(request,'media.html',{'posts':posts})

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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    return render(request, 'BPO-services.html')
# Background Verifications
def backgoundVerification(request):
    if request.method == 'POST':
        form_name = 'BPO-service'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phoneNo']
        jobTitle = request.POST['job_title']
        select = request.POST['select']
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    return render(request, 'backgoundVerification.html')
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
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
        return render(request, 'success.html', {'message':'Request has been sent !',"name":first_name,'info':'our team will be contact you within 24:00 Hours.'})
    else:
        return render(request,'web-development.html')
    

    # energy services=======================================================
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

        form_name = 'wind-energy'
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

        form_name = 'Thermal-energy'
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

        form_name = 'recruit-management'
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

        form_name = 'Human-Resource'
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


# investors

def investors(request):
    return render(request, 'investors.html')

def insights(request):
    return render(request, 'insights.html')
# admin details and fetch..data

from .models import HomeContact, ContactUs, SignInUser, ContactMessage, Industries, Energy, Products, MediaPost, Job, JobApply
def adminHome(request):
    return render(request,'TSARIT-dashboard.html')

def Dashboard(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == 'tsaritservices@gmail.com' and password == 'tsarit@12345':
            #  fetching the data if user authenticated
           
            #  home page contact data
             homePage = HomeContact.objects.all()

            #  services page data
             web = ContactMessage.objects.filter(form_name = 'web-service').order_by('id')
             app = ContactMessage.objects.filter(form_name = 'app-service').order_by('id')
             bpo = ContactMessage.objects.filter(form_name = 'BPO-service').order_by('id')
             sateliteServ = ContactMessage.objects.filter(form_name = 'satelite-service').order_by('id')
             civil = ContactMessage.objects.filter(form_name = 'civil-service').order_by('id')
             mpn = ContactMessage.objects.filter(form_name = 'man-power-supply-service').order_by('id')
             payRoll = ContactMessage.objects.filter(form_name = 'payRoll-service').order_by('id')
             ngo = ContactMessage.objects.filter(form_name = 'NGO-service').order_by('id')
             photoVideo = ContactMessage.objects.filter(form_name = 'photo&Video-service').order_by('id')
             dm = ContactMessage.objects.filter(form_name = 'digital-Marketing-service').order_by('id')
             survey = ContactMessage.objects.filter(form_name = 'survey-service').order_by('id')
             distrib = ContactMessage.objects.filter(form_name = 'distribution-service').order_by('id')

            #  industries pages data
             aero = Industries.objects.filter(form_name = 'Aerospace-industry').order_by('id')
             auto = Industries.objects.filter(form_name = 'autoMotive-industry').order_by('id')
             bank = Industries.objects.filter(form_name = 'banking-industry').order_by('id')
             capital = Industries.objects.filter(form_name = 'capitalMarket-industry').order_by('id')
             cmnctn = Industries.objects.filter(form_name = 'Communications-industry').order_by('id')
             consumer = Industries.objects.filter(form_name = 'ConsumerElectronics-industry').order_by('id')
             cpg = Industries.objects.filter(form_name = 'consumerPackagedGoods-industry').order_by('id')
             edu = Industries.objects.filter(form_name = 'Education-industry').order_by('id')
             eoi = Industries.objects.filter(form_name = 'EngineeringOperations-industry').order_by('id')
             health = Industries.objects.filter(form_name = 'healthCare-industry').order_by('id')
             iProcess = Industries.objects.filter(form_name = 'IndustrialProcess-industry').order_by('id')
             insurance = Industries.objects.filter(form_name = 'insurance-industry').order_by('id')
             pharma = Industries.objects.filter(form_name = 'LifePharma-industry').order_by('id')
             media = Industries.objects.filter(form_name = 'MediaServices-industry').order_by('id')
             natural = Industries.objects.filter(form_name = 'NaturalResources-industry').order_by('id')
             network = Industries.objects.filter(form_name = 'NetworkEdgeProviders-industry').order_by('id')
             oilGasss = Industries.objects.filter(form_name = 'oilGas-industry').order_by('id')
             software = Industries.objects.filter(form_name = 'SoftwareProducts-industry').order_by('id')
             professional = Industries.objects.filter(form_name = 'ProfessionalServices-industry').order_by('id')
             publicSector = Industries.objects.filter(form_name = 'PublicSector-industry').order_by('id')
             retail = Industries.objects.filter(form_name = 'Retail-industry').order_by('id')
             semiC = Industries.objects.filter(form_name = 'Semiconductors-industry').order_by('id')
             transport = Industries.objects.filter(form_name = 'TransportationServices-industry').order_by('id')
             utilities = Industries.objects.filter(form_name = 'Utilities-industry').order_by('id')

            #  Energy

             solar =Energy.objects.filter(form_name = 'solar-energy').order_by('id')
             wind = Energy.objects.filter(form_name = 'wind energy').order_by('id')
             thermal = Energy.objects.filter(form_name = 'Thermal-energy').order_by('id')

            #  conact us
             conact = ContactUs.objects.all().order_by('id')
             len_conact = len(conact)

            # products data
             hms = Products.objects.filter(form_name = 'Hospital Management System').order_by('id')
             chatbot = Products.objects.filter(form_name = 'AI-Chatbot').order_by('id')
             ems = Products.objects.filter(form_name = 'Education Management System').order_by('id')
             fms = Products.objects.filter(form_name = 'finance Management System').order_by('id')
             rms = Products.objects.filter(form_name = 'recruit-management').order_by('id')
             hrm = Products.objects.filter(form_name = 'Human-Resource').order_by('id')

            # job apply

             jobsApply = JobApply.objects.all().order_by('id')
             len_jobApply = len(jobsApply)

            # combining the all tables

             all_Services = list(web) + list(app) + list(bpo) + list(sateliteServ) + list(civil)+list(mpn)+list(payRoll)+list(ngo)+list(photoVideo)+list(dm)+list(survey)+list(distrib)
             allServicsCount = len(all_Services)

             all_industries = list(aero) + list(auto) + list(bank) + list(capital) + list(cmnctn) + list(consumer) + list(cpg) + list(edu) + list(eoi) + list(health) + list(iProcess) + list(insurance) + list(pharma) + list(media) + list(natural) + list(network) + list(oilGasss) + list(software) + list(professional) + list(publicSector) + list(retail) + list(semiC) + list(transport) + list(utilities)
             industries_length = len(all_industries)

             all_energy = list(solar) + list(wind) + list(thermal)
             energy_len = len(all_energy)

            #  products
             all_products = list(hms) + list(chatbot) + list(ems) + list(fms) + list(rms) + list(hrm)
             products_count = len(all_products)
             
          

             return render(request,'TSARIT-dashboard.html',{
                 "homePage":homePage,

                #  servces pages data fetch
                 'allServices':all_Services,
                 'allServicsCount':allServicsCount,

                #  industries data fetch
                "all_industries":all_industries,
                "industries_length":industries_length,

                # energy
                "all_energy":all_energy,
                "energy_len":energy_len,

                # conact us
                "conact":conact,
                "len_conact":len_conact,

                # products
                "all_products":all_products,
                "products_count":products_count,

                # jobs apply perosons
                'jobsApply':jobsApply,
                'len_jobApply':len_jobApply
                 })
        else:
            # else for returning into login if pswd or email wrong.....................................
            messages =  'Invalid email or password.'
    return render(request, 'adminLogin.html')

from django.contrib.auth import logout as django_logout

def logout(request):
    django_logout(request)
    return render(request, 'adminLogin.html')

def adminLogin(request):
    return render(request,'adminLogin.html')


def searchService(request):
    if request.method == 'POST':
        searchInp = request.POST['serviceInput']
        fetchData = ContactMessage.objects.filter(form_name =searchInp)

        return render(request, 'TSARIT-dashboard.html',{'fetchData':fetchData})

# media page


from .forms import MediaPostForm


def media_page(request):
    form = MediaPostForm()
    posts = MediaPost.objects.all()

    if request.method == 'POST':
        form = MediaPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_page')

    context = {'form': form, 'posts': posts}
    return render(request, 'media_page.html', context)

def update_post(request, pk):
    post = get_object_or_404(MediaPost, pk=pk)
    form = MediaPostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('media_page')

    return render(request, 'media_page.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(MediaPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('media_page')

    return render(request, 'media_page.html', {'post': post})

#  job posting

from app.models import Job

def JobPosting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        skills = request.POST.get('skills')
        date = request.POST.get('date')
        jobs = Job.objects.create(title=title,description=description,location=location,company=company,salary=salary,skills=skills,date=date)
        jobs.save()
        return render(request,'TSARIT-dashboard.html')
    return render(request,'TSARIT-dashboard.html')
