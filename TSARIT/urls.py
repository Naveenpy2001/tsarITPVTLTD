"""
URL configuration for TSARIT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importing views from app
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('header',views.header),

    path('about',views.about),
    path('conactForm',views.conactForm),
    path('accessbility',views.accessbility),
    path('accountsDashboard',views.accountsDashboard),
    path('Aerospace',views.Aerospace),
    path('chatbot',views.chatbot),
    path('angular',views.angular),
    path('appDevelopment',views.appDevelopment),
    path('automotive',views.automotive),
    path('aws',views.aws),
    path('azure',views.azure),
    path('Banking',views.Banking),
    path('bigdata',views.bigdata),
    path('BPOservices',views.BPOservices),
    path('capitalMarket',views.capitalMarket),
    path('civilConstructions',views.civilConstructions),
    path('Communications',views.Communications),
    path('ConsumerElectronics',views.ConsumerElectronics),
    path('consumerPackagedGoods',views.consumerPackagedGoods),
    path('cloud',views.cloud),
    path('Communications',views.Communications),
    path('ConsumerElectronics',views.ConsumerElectronics),
    path('contact',views.contact),
    path('coockiesPolicy',views.coockiesPolicy),
    path('CorporateLogin',views.CorporateLogin),
    path('csr',views.csr),
    path('dataScience',views.dataScience),
    path('digitalmarketing',views.digitalmarketing),
    path('distribution',views.distribution),
    path('dotnet',views.dotnet),
    path('Education',views.Education),
    path('EMS',views.EMS),
    path('EngineeringOperations',views.EngineeringOperations),
    path('financeManagement',views.financeManagement),
    path('HealthCare',views.HealthCare),
    path('hrManagement',views.hrManagement),
    path('hrDashboard',views.hrDashboard),
    path('HMS',views.HMS),
    path('IndustrialProcess',views.IndustrialProcess),
    path('insurance',views.insurance),
    path('internshipPage',views.internshipPage),
    path('ItPromotions',views.ItPromotions),
    path('Java',views.Java),
    path('jobApply/<int:job_id>/',views.jobApply,name='jobApply'),
    path('jobPage',views.jobPage),
    path('LifePharma',views.LifePharma),
    path('manPowerSupply',views.manPowerSupply),
    path('marketDashboard',views.marketDashboard),
    path('Media',views.Media,name="Media"),
    path('MediaServices',views.MediaServices),
    path('mediaDashboard',views.mediaDashboard),
    path('NaturalResources',views.NaturalResources),
    path('NetworkProviders',views.NetworkProviders),
    path('NGO',views.NGO),
    path('oilGas',views.oilGas),
    path('PayrollJobs',views.PayrollJobs),
    path('photo_edting',views.photo_edting),
    path('php',views.php),
    path('SoftwareProducts',views.SoftwareProducts),
    path('privacypolicy',views.privacypolicy),
    path('ProfessionalServices',views.ProfessionalServices),
    path('profileDashboard',views.profileDashboard),
    path('PublicSector',views.PublicSector),
    path('pythonPage',views.pythonPage),
    path('reactJs',views.reactJs),
    path('recruitmanagement',views.recruitmanagement),
    path('registrationForm',views.registrationForm),
    path('Retail',views.Retail),
    path('salesforce',views.salesforce),
    path('sap',views.sap),
    path('satelite',views.satelite),
    path('securityNotifications',views.securityNotifications),
    path('Semiconductors',views.Semiconductors),
    path('solar',views.solar),
    path('studentDashboard',views.studentDashboard),
    path('studentLogin',views.studentLogin),
    path('Survey',views.Survey),
    path('TermsUse',views.TermsUse),
    path('thermal',views.thermal),
    path('trainerDashboard',views.trainerDashboard),
    path('TransportationServices',views.TransportationServices),
    path('Utilities',views.Utilities),
    path('webDevelopment',views.webDevelopment),
    path('wind',views.wind),
    path('LifteAtTSARIT',views.LifteAtTSARIT),

    # main URLs 
    # home page
    path('indexContact',views.indexContact,name='indexContact'),
    path('success/', views.success_view, name='success'),
    path('signInStudent', views.signInStudent, name='signInStudent'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('logOut_student', views.logOut_student, name='logOut_student'),
    # service URLs
    path('serviceWebDev', views.serviceWebDev, name='serviceWebDev'),
    path('AppDevService', views.AppDevService, name='AppDevService'),
    path('ServiceBPO', views.ServiceBPO, name='ServiceBPO'),
    path('sateliteServices', views.sateliteServices, name='sateliteServices'),
    path('civilService', views.civilService, name='civilService'),
    path('ManPowerService', views.ManPowerService, name='ManPowerService'),
    path('payRollServ', views.payRollServ, name='payRollServ'),
    path('NGOservice', views.NGOservice, name='NGOservice'),
    path('PhotoVideoService', views.PhotoVideoService, name='PhotoVideoService'),
    path('DigitalMarketingServ', views.DigitalMarketingServ, name='DigitalMarketingServ'),
    path('SurveyService', views.SurveyService, name='SurveyService'),
    path('distributionService', views.distributionService, name='distributionService'),

    # industry page form URLs
    path('aeroIndustry', views.aeroIndustry, name='aeroIndustry'),

    path('automotivendustry', views.automotivendustry, name='automotivendustry'),
    
    path('bankIndustry', views.bankIndustry, name='bankIndustry'),
    
    path('capitalIndustry', views.capitalIndustry, name='capitalIndustry'),
    
    path('communicationsIndustry', views.communicationsIndustry, name='communicationsIndustry'),
    
    path('consumerIndustry', views.consumerIndustry, name='consumerIndustry'),

    path('cPackagedIndustry', views.cPackagedIndustry, name='cPackagedIndustry'),

    path('educationIndustry', views.educationIndustry, name='educationIndustry'),

    path('eng_operationIndustry', views.eng_operationIndustry, name='eng_operationIndustry'),

    path('healthCareIndustry', views.healthCareIndustry, name='healthCareIndustry'),

    path('industrialProcInd', views.industrialProcInd, name='industrialProcInd'),

    path('insuranceIndustry', views.insuranceIndustry, name='insuranceIndustry'),

    path('pharmaIndustry', views.pharmaIndustry, name='pharmaIndustry'),

    path('mediaIndustry', views.mediaIndustry, name='mediaIndustry'),

    path('naturalResIndustry', views.naturalResIndustry, name='naturalResIndustry'),

    path('networkIndustry', views.networkIndustry, name='networkIndustry'),

    path('oilGasIndustry', views.oilGasIndustry, name='oilGasIndustry'),

    path('softwareProductsIndustry', views.softwareProductsIndustry, name='softwareProductsIndustry'),

    path('serviceIndustry', views.serviceIndustry, name='serviceIndustry'),

    path('publicSectorIndustry', views.publicSectorIndustry, name='publicSectorIndustry'),

    path('retailIndustry', views.retailIndustry, name='retailIndustry'),

    path('semiConductorsIndustry', views.semiConductorsIndustry, name='semiConductorsIndustry'),

    path('transportIndustry', views.transportIndustry, name='transportIndustry'),

    path('utilitiesIndustry', views.utilitiesIndustry, name='utilitiesIndustry'),

    # energy URL's

    path('solaarEn', views.solaarEn, name='solaarEn'),

    path('windEnergy', views.windEnergy, name='windEnergy'),

    path('thermalEnergy', views.thermalEnergy, name='thermalEnergy'),

    
    # produtcs URL's

    path('hospitalMS', views.hospitalMS, name='hospitalMS'),

    path('AIchatBot', views.AIchatBot, name='AIchatBot'),

    path('educationMS', views.educationMS, name='educationMS'),

    path('FMS', views.FMS, name='FMS'),

    path('RMS', views.RMS, name='RMS'),

    path('HRM', views.HRM, name='HRM'),

    # path('resume/<int:applicant_id>/', views.display_resume, name='display_resume'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)