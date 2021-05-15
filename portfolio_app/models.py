from django.db import models
from django.conf import settings
# Create your models here.

class projects(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='image')

    @staticmethod
    def get_all_project():
        return projects.objects.all().order_by('-id')[:8]

    def __str__(self):
        return self.title

class certificate(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    images = models.ImageField(upload_to='images')

    @staticmethod
    def get_all_certificate():
        return certificate.objects.all()

    def __str__(self):
        return self.title


class Contacts(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    Messages = models.TextField(max_length=400)

    @staticmethod
    def get_all_Contacts():
        return Contacts.objects.all()

    def __str__(self):
        return self.Name
    


class Blogs(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    images = models.ImageField(upload_to='images', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, default=False)
    author = models.CharField(max_length=100, null=True)

    @staticmethod
    def get_all_Blogs():
        return Blogs.objects.all().order_by('-pub_date')[:10]


    def summary(self):
        return self.body[:80]

    def __str__(self):
        return self.title