
from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('submit', views.submit_form, name='submit_form'),
    path('newpage',views.form_view,name='form_view'),
    path('course_view', views.course_view, name='course_view'),
    #############################
    path('subject',views.subject,name='subject'),
    path('loadcourse', views.loadcourse, name='loadcourse'),
    
]