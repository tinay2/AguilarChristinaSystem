from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Appointment



    
    

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_list.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['customer','service', 'date', 'time', 'status', 'total_price']
    template_name = 'app/appointment_create.html'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['customer','service', 'date', 'time', 'status', 'total_price']
    template_name = 'app/appointment_update.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')