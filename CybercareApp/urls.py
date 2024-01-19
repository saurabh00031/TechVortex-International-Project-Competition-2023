from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('malware_detection/', views.malware_detection, name='malware_detection'),
    path('detect_malware/', views.detect_malware, name='detect_malware'),
    path('url_detection/', views.url_detection, name='url_detection'),
    path('password_generator/',views.password_generator,name="password_generator"),
    path('contact_page/',views.contact_page,name="contact_page")


 
]