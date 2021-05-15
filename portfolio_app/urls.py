from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.main_page,name='main_page'),

    path('home_page', views.home,name='home_page'),

    path('project_page', views.project, name='project_page'),

    path('certificates_page', views.certificates, name='certificates_page'),

    path('contact_page', views.contact, name='contact_page'),

    path('blogs_page', views.blogs, name='blogs_page'),
]