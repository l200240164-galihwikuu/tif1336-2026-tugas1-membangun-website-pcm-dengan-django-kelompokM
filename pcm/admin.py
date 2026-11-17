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

@admin.register(FotoKondisi)
class FotoKondisiAdmin(admin.ModelAdmin):
    list_display = ("id", "keterangan", "urutan")
    list_filter = ()
    ordering = ("urutan", "id")


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

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("nama_kegiatan", "waktu_mulai", "tempat")
    search_fields = ("nama_kegiatan", "tempat")
    date_hierarchy = "waktu_mulai"


@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ("judul", "tanggal_unggah")
    list_filter = ("tanggal_unggah",)
    search_fields = ("judul", "keterangan")
    date_hierarchy = "tanggal_unggah"


@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ("nama", "email", "subjek", "waktu_kirim", "sudah_dibaca")
    list_filter = ("sudah_dibaca", "waktu_kirim")
    search_fields = ("nama", "email", "subjek")
    date_hierarchy = "waktu_kirim"
    list_editable = ("sudah_dibaca",)

    @admin.action(description="Tandai sudah dibaca")
    def tandai_dibaca(self, request, queryset):
        queryset.update(sudah_dibaca=True)

    @admin.action(description="Tandai belum dibaca")
    def tandai_belum_dibaca(self, request, queryset):
        queryset.update(sudah_dibaca=False)

    actions = ["tandai_dibaca", "tandai_belum_dibaca"]
