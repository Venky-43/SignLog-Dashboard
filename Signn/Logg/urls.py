from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_view, name='login'),
    path('patient/<str:username>/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/<str:username>/', views.doctor_dashboard, name='doctor_dashboard'),
]
