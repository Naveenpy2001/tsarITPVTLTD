from django.db import models

# Create your models here.

class HomeContact(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField()
    busines_email = models.EmailField()
    userphno = models.CharField(max_length=20)
    userjob = models.CharField(max_length=150)
    userCompany = models.CharField(max_length=160)
    message = models.TextField()


class SignInUser(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)


# services
    
class ContactMessage(models.Model):
    form_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    jobTitle = models.CharField(max_length=100)
    select = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.form_name} - {self.name}"