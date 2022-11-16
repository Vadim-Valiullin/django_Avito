import csv
import json

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('csv_files/datasets/ads.csv', encoding='utf-8') as csv_ads:
            with open('csv_files/datasets/ads.json', 'w', encoding='utf-8') as js_ads:
                json.dump(list(csv.DictReader(csv_ads)), js_ads, ensure_ascii=False)

        with open('csv_files/datasets/categories.csv', encoding='utf-8') as csv_cat:
            with open('csv_files/datasets/categories.json', 'w', encoding='utf-8') as js_cat:
                json.dump(list(csv.DictReader(csv_cat)), js_cat, ensure_ascii=False)
