from django.urls import path

from . import views

app_name = "pcm"

urlpatterns = [
    path("", views.beranda, name="beranda"),
    path("profil/", views.profil_organisasi, name="profil"),
    path("pimpinan/", views.daftar_pimpinan, name="pimpinan"),
    path("ranting/", views.daftar_ranting, name="ranting"),
    path("amal-usaha/", views.daftar_amal_usaha, name="amal_usaha"),
    path("berita/", views.daftar_berita, name="berita"),
    path("berita/<slug:slug>/", views.detail_berita, name="detail_berita"),
    path("agenda/", views.daftar_agenda, name="agenda"),
    path("dokumen/", views.daftar_dokumen, name="dokumen"),
    path("kontak/", views.kontak, name="kontak"),
]