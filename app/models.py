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

class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    usersubject = models.CharField(max_length=150)
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
    
class Industries(models.Model):
    form_name = models.CharField(max_length=100)
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
    
class Energy(models.Model):
    form_name = models.CharField(max_length=100)
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
    

    
class Products(models.Model):
    form_name = models.CharField(max_length=100)
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
    
# class MediaPost(models.Model):
#     title = models.CharField(max_length=100)
#     image1 = models.ImageField(upload_to='uploads/')
#     image2 = models.ImageField(upload_to='uploads/')
#     narration = models.TextField()

#     def __str__(self):
#         return self.title
    

# job posting

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        


class JobApply(models.Model):
    form_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200,null=True)
    country_code = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    aadhar_card_number = models.CharField(max_length=200, null=True)
    is_fresher = models.CharField(max_length=200, null=True)
    applied_with_tsar_it = models.CharField(max_length=200, null=True)
    previous_employee_id = models.CharField(max_length=200, null=True)
    resume = models.FileField(upload_to='resumes/')
    terms_of_use_agreed = models.CharField(max_length=200, null=True)


class MediaPost(models.Model):
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='uploads/')
    image2 = models.ImageField(upload_to='uploads/')
    narration = models.TextField()

    def __str__(self):
        return self.title