from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Agenda, AmalUsaha, Berita, Pimpinan, ProfilOrganisasi, Ranting, FotoKondisi


def beranda(request):
    konteks = {
        # Berita
        "berita_terbaru": Berita.objects.terbit()[:3],

        # Agenda
        "agenda_mendatang": Agenda.objects.filter(
            waktu_mulai__gte=timezone.now()
        )[:3],

        # Statistik
        "jumlah_ranting": Ranting.objects.count(),
        "jumlah_amal_usaha": AmalUsaha.objects.count(),
        "jumlah_pimpinan": Pimpinan.objects.count(),

        # Pimpinan di halaman utama
        "daftar_pimpinan": Pimpinan.objects.order_by(
            "urutan", "nama"
        )[:3],
    }

    return render(request, "pcm/beranda.html", konteks)



def profil_organisasi(request):
    profil = ProfilOrganisasi.objects.first()
    foto_kondisi = FotoKondisi.objects.all()

    konteks = {
        "profil": profil,
        "daftar_pimpinan": Pimpinan.objects.all(),
        "foto_kondisi": foto_kondisi,
    }

    return render(request, "pcm/profil.html", konteks)


def daftar_pimpinan(request):
    return render(request, "pcm/pimpinan.html", {"daftar_pimpinan": Pimpinan.objects.all()})

def daftar_ranting(request):
    return render(request, "pcm/ranting.html", {"daftar_ranting": Ranting.objects.all()})


def daftar_amal_usaha(request):
    bidang = request.GET.get("bidang", "")
    daftar = AmalUsaha.objects.all()
    if bidang in AmalUsaha.Bidang.values:
        daftar = daftar.filter(bidang=bidang)
    else:
        bidang = ""
    return render(request, "pcm/amal_usaha.html", {
        "daftar_amal_usaha": daftar,
        "bidang_terpilih": bidang,
        "pilihan_bidang": AmalUsaha.Bidang.choices,
    })

def daftar_berita(request):
    return render(request, "pcm/berita.html", {"daftar_berita": Berita.objects.terbit()})


def detail_berita(request, slug):
    berita = get_object_or_404(Berita.objects.terbit(), slug=slug)

    berita_lain = Berita.objects.terbit().exclude(
        pk=berita.pk
    ).order_by("-tanggal_terbit")[:3]

    return render(request, "pcm/detail_berita.html", {
        "berita": berita,
        "berita_lain": berita_lain,
    })


def daftar_agenda(request):
    agenda_list = Agenda.objects.filter(waktu_mulai__gte=timezone.now())
    return render(request, "pcm/agenda.html", {"daftar_agenda": agenda_list})


