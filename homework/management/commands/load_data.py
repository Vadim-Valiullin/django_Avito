from django.core.management import BaseCommand
import json
from homework.models import Ads, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:

            with open('csv_files/datasets/categories.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    cat_for_table = Category(
                        name=d['name'],
                    )
                    cat_for_table.save()

            with open('csv_files/datasets/ads.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    ads_for_table = Ads(
                        name=d['name'],
                        author=d['author'],
                        price=d['price'],
                        description=d['description'],
                        address=d['address'],
                        is_published=d['is_published'].lower().title(),
                    )
                    ads_for_table.save()


            print('insert done')
        except:
            print('insert failed')

