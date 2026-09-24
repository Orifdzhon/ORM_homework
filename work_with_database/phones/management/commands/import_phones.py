import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Phone


class Command(BaseCommand):
    help = "Import phones from phones.csv"

    def handle(self, *args, **options):
        csv_path = Path(settings.BASE_DIR) / "phones.csv"

        with open(csv_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                Phone.objects.update_or_create(
                    id=row["id"],
                    defaults={
                        "name": row["name"],
                        "image": row["image"],
                        "price": row["price"],
                        "release_date": row["release_date"],
                        "lte_exists": row["lte_exists"].lower() == "true",
                    },
                )

        self.stdout.write(self.style.SUCCESS("Phones imported successfully."))