from django.db import models

# Create your models here.

class customer (models.Model):
    comp_name = models.CharField(max_length=200, null=True)
    college = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    course = models.CharField(max_length=200, null=True)
    Views = models.CharField(max_length=200, null=True)
    Date_Created =models.DateTimeField(auto_now_add = True, null=True) 


    def __str__(self):
        return self.name

class customer_comp (models.Model):
    comp_name = models.CharField(max_length=200, null=True)
    Area = models.CharField(max_length= 200 , null=True)


    def __str__(self):
        return self.comp_name

class Experience (models.Model):
    experience = models.CharField(max_length=20000, null=True)
    rating = models.CharField(max_length = 200 , null=True)


    def __str__(self):
        return self.experience

class Job_type (models.Model):
    JOB_TYPE = (('Summer Internship', 'Summer Internship'),
            ('Winter Internship and Job', 'Winter Internship and Job'),
            ('Job only','Job only'))
    jobType = models.CharField(max_length=200, null=True, choices=JOB_TYPE)


    def __str__(self):
        return self.jobType
        
class job_profile (models.Model):
    jobProfile = models.CharField(max_length=20000, null=True)
    
    def __str__(self):
        return self.jobProfile

class new (models.Model):
    JOB_TYPE = (('Summer Internship', 'Summer Internship'),
                ('Winter Internship and Job', 'Winter Internship and Job'),
                ('Job only','Job only'),
                ('Winter Internship only','Winter Internship only'))
    comp_name = models.CharField (max_length=200, null=True)
    year = models.CharField (max_length=200, null=True)
    job_type = models.CharField (max_length=200, null=True) 
    job_profile = models.CharField (max_length=200, null=True,choices=JOB_TYPE)

    customer = models.ForeignKey(customer , null=True, on_delete=models.SET_NULL)

class main_customer (models.Model):
    comp_name = models.CharField(max_length=200, null=True)
    college = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    course = models.CharField(max_length=200, null=True)
    Views = models.CharField(max_length=200, null=True)
    Date_Created =models.DateTimeField(auto_now_add = True, null=True) 


    def __str__(self):
        return self.name



    