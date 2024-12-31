from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from .views import HomePageView, AboutPageView 
from .views import (
    AppointmentListView, 
    AppointmentDetailView, 
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView, 

)





urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    
    path('appointment/', AppointmentListView.as_view(), name='appointment'),    
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('appointment/', AppointmentListView.as_view(), name='appointment_list'),
   


   
]