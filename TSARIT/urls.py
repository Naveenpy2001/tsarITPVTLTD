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
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('header',views.header),

    path('about',views.about),
    path('accessbility',views.accessbility),
    path('accountsDashboard',views.accountsDashboard),
    path('adminLogin',views.adminLogin),
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
    path('jobApply',views.jobApply),
    path('jobPage',views.jobPage),
    path('LifePharma',views.LifePharma),
    path('manPowerSupply',views.manPowerSupply),
    path('marketDashboard',views.marketDashboard),
    path('media',views.media),
    path('MediaServices',views.MediaServices),
    path('mediaDashboard',views.mediaDashboard),
    path('NaturalResources',views.NaturalResources),
    path('NetworkProviders',views.NetworkProviders),
    path('NGO',views.NGO),
    path('oilgas',views.oilgas),
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
    path('TSARITdashboard',views.TSARITdashboard),
    path('Utilities',views.Utilities),
    path('webDevelopment',views.webDevelopment),
    path('wind',views.wind),
    path('notFound',views.Banking),

    # main URLs 

    path('indexContact',views.indexContact,name='indexContact'),
    path('success/', views.success_view, name='success'),
    path('signInStudent', views.signInStudent, name='signInStudent'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('logOut_student', views.logOut_student, name='logOut_student'),
    path('serviceWebDev', views.serviceWebDev, name='serviceWebDev'),
    path('AppDevService', views.AppDevService, name='AppDevService'),
    path('ServiceBPO', views.ServiceBPO, name='ServiceBPO'),
    path('sateliteServices', views.sateliteServices, name='sateliteServices'),
    path('civilService', views.civilService, name='civilService'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)