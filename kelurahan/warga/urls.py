from django.urls import path
from .views import WargaListView
from .views import WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView, WargaUpdateView, WargaDeleteView, PengaduanUpdateView, PengaduanDeleteView 

urlpatterns = [
    path('warga/', WargaListView.as_view(), name="warga-list"),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('<int:pk>/warga/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/warga/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    path('<int:pk>/pengaduan/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('<int:pk>/pengaduan/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
      
]