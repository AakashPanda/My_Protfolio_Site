from django.shortcuts import render, redirect

# Create your views here.

from .models import projects,certificate,Contacts,Blogs
from django.conf import settings 
from django.core.mail import send_mail

def home(request):
    return render(request, 'Mypage.html')

def main_page(request): 
    projects_ = projects.get_all_project()
    certificate_ = certificate.get_all_certificate()
    Contacts_= Contacts.get_all_Contacts()
    Blogs_=Blogs.get_all_Blogs()
    num_of_certificate = len(certificate_)
    num_of_project = len(projects_)
    num_of_Contacts = len(Contacts_)
    num_of_Blogs = len(Blogs_)
    context = {
        'projects': projects_,

        'Blogs': Blogs_,
        'num_of_projects': num_of_project,
        'num_of_certificate': num_of_certificate,
        'num_of_Contacts': num_of_Contacts,
        'num_of_Blogs':num_of_Blogs,
    }
    if request.method == 'POST':
        Your_name = request.POST['Name']
        Email_address = request.POST['Email']
        Subject_name = request.POST['Subject']
        Your_Meassage = request.POST['Message']
        var_contact = Contacts(Name = Your_name,Email=Email_address,subject=Subject_name,Messages=Your_Meassage)
        var_contact.save()   
        
        message = f'{Your_name} has Sent You an Email, \n\nEmail : {Email_address}\n\n{Your_Meassage}'
        send_mail(
            Subject_name,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
    

        )

        return render(request, 'Contact/Thanks_page.html')
    
    return render(request, 'HomePage.html', context)

    

def project(request):
    num = projects.objects.all().order_by('-id')
    return render(request, 'Projects.html',{'nums': num})


def certificates(request):
    cer =certificate.objects.all()
    return render(request,'Certificates.html',{'blog': cer})


def contact(request):
    if request.method == 'POST':
        Your_name = request.POST['Name']
        Email_address = request.POST['Email']
        Subject_name = request.POST['Subject']
        Your_Meassage = request.POST['Message']
        var_contact = Contacts(Name = Your_name,Email=Email_address,subject=Subject_name,Messages=Your_Meassage)
        var_contact.save()   

        message = f'{Your_name} has Sent You an Email, \n\nEmail : {Email_address}\n\n{Your_Meassage}'
        send_mail(
            Subject_name,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
    

        )
         
        return render(request, 'Contact/Thanks_page.html')
    else:
        return render(request, 'Contact/contact_us.html')
    

def blogs(request):
    var_1 = Blogs.objects.all().order_by('-pub_date')   
    if request.method == 'POST':
        title= request.POST['title']
        author = request.POST['author']
        Your_Message = request.POST['message']
        thumbnail = request.FILES.get('thumbnail')
        var_blog = Blogs(title = title, body=Your_Message, author=author, images=thumbnail)
        var_blog.save()  
         
        message = f'{author} has Posted {title} - blog, \n\n{Your_Message}'
        send_mail(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
    

        )
        return redirect('blogs_page')

    return render(request, 'Blogs.html',{'var':var_1})
  
     