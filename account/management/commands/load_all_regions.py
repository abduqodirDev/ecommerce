import json

from django.core.management import BaseCommand

from common.models import Country, Region
from config.settings.base import BASE_DIR


class Command(BaseCommand):
    help = "load all regions"

    def handle(self, *args, **options):
        try:
            with open(str(BASE_DIR) + "/data/regions.json", encoding='utf-8') as f:
                regions = json.load(f)
                country = Country.objects.get(name="O'zbekiston")
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)

            self.stdout.write(self.style.SUCCESS("Regions loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

