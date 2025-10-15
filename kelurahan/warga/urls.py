from django.urls import path
from .views import WargaListView
from .views import WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView

urlpatterns = [
    path('warga/', WargaListView.as_view(), name="warga-list"),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]