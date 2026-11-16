from django.contrib import admin

from .models import (
    Agenda,
    AmalUsaha,
    Berita,
    Dokumen,
    PesanMasuk,
    Pimpinan,
    ProfilOrganisasi,
    Ranting,
    TautanTerkait,
    FotoKondisi,
)

admin.site.site_header = "Admin Website PCM"
admin.site.site_title = "Admin PCM"
admin.site.index_title = "Kelola Website"

@admin.register(ProfilOrganisasi)
class ProfilOrganisasiAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_singkat", "telepon", "email")

    def has_add_permission(self, request):
        return not ProfilOrganisasi.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "periode", "urutan")
    list_editable = ("urutan",)
    search_fields = ("nama", "jabatan")

@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ("nama", "ketua", "telepon")
    search_fields = ("nama", "ketua")


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ("nama", "bidang", "alamat")
    list_filter = ("bidang",)
    search_fields = ("nama",)

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "status", "tanggal_terbit")
    list_filter = ("status",)
    search_fields = ("judul", "ringkasan")
    prepopulated_fields = {"slug": ("judul",)}
    date_hierarchy = "tanggal_terbit"