from .models import ProfilOrganisasi


def organisasi(request):
    return {"profil": ProfilOrganisasi.objects.first()}
