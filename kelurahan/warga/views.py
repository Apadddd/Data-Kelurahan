from django.shortcuts import render
from django.views.generic import ListView
from .models import Warga, Pengaduan
from django.views.generic import DetailView

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan