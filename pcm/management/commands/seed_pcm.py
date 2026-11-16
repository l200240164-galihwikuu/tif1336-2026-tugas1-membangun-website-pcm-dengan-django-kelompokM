from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Mengisi data awal website PCM dari pcm/fixtures/data_awal.json"

    def handle(self, *args, **options):
        call_command("loaddata", "data_awal.json")
        self.stdout.write(self.style.SUCCESS("Data awal PCM berhasil dimuat."))