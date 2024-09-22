import json

from django.core.management import BaseCommand

from common.models import Country
from config.settings.base import BASE_DIR


class Command(BaseCommand):
    help = "load all countries"

    def handle(self, *args, **options):
        try:
            with open(str(BASE_DIR) + "/data/countries.json", encoding='utf-8') as f:
                countries = json.load(f)
                for country in countries:
                    Country.objects.get_or_create(name=country['name_uz'], code=country['code'])

            self.stdout.write(self.style.SUCCESS("Countries loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

