from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Data
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data
# Create your views here.



class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('id')
    serializer_class = DataSerializer

class DataListView(ListView):
    model = Data
    template_name = 'data-list.html'

class DataCreateView(CreateView):
    model = Data
    template_name = 'data-create.html'
    fields = ('temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation', 'captured_sensor_time_date')
    success_url = reverse_lazy('data-list')

class DataDetailView(DetailView):
    model = Data
    template_name = 'data-detail.html'

class DataUpdateView(UpdateView):
    model = Data
    template_name = 'data-update.html'
    fields = ('temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation', 'captured_sensor_time_date')
    success_url = reverse_lazy('data-list')

class DataDeleteView(DeleteView):
    model = Data
    template_name = 'data-delete.html'
    success_url = reverse_lazy('data-list')
def show(request):
    # table = Data.objects.all()
    table_abc = Data.objects.all().order_by('-id')[:3]
    table = reversed(table_abc)
    return render(request,"show.html",{'object_list':table})

def graph(request):
    qs= Data.objects.all().order_by('-id')[:5]
    # abc = Data.objects.all().order_by('-id')[:3]
    # qs = reversed(abc)
    return render(request,"chart.html",{'object_list':qs})
#
# class DataChartView(TemplateView):
#     model = Data
#     template_name = 'chart.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['qs'] = Data.objects.all()
#         return context
