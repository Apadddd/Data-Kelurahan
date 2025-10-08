from django.urls import path
from .views import WargaListView
from .views import WargaDetailView, PengaduanListView

urlpatterns = [
    path('warga/', WargaListView.as_view(), name="warga-list"),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
]