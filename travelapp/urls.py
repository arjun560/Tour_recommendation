from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('fyp/', views.fyp, name='fyp'),
    path('service/', views.service, name='service'),
    path('login/', views.login, name='login'),
    path('recomendations/', views.recomendations, name='recomendations'),
    path('contact/', views.contact, name='contact'),
    path('userdash/', views.userdash, name='userdash'),
    path('favlocation/', views.favlocation, name='favlocation'),
    path('recentrecom/', views.recentrecom, name='recentrecom'),
    path('support/', views.support, name='support'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('profile/', views.profile, name='profile'),
]