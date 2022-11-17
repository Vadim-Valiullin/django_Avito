from django.shortcuts import render

import json

from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import DetailView

from homework.models import Ads, Category


def index(request):
    return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads_res = Ads.objects.all()
        ads_list = []
        for ad in ads_res:
            ads_list.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })

        return JsonResponse(ads_list, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ads = Ads(
            name=data['name'],
            price=data['price'],
            author=data['author'],
            description=data['description'],
            address=data['address'],
            is_published=data['is_published'],
        )
        ads.save()
        return JsonResponse({'res': 'ok'})


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse({
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            'address': ad.address,
            "is_published": ad.is_published,
        })

    
@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        cat_res = Category.objects.all()
        cat_list = []
        for cat in cat_res:
            cat_list.append({
                "id": cat.id,
                "name": cat.name,
            })

        return JsonResponse(cat_list, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category(
            name=data['name'],
        )
        cat.save()
        return JsonResponse({'res': 'ok'})


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })
#
#
# def adv_id(request, adv_id):
#     adv_res = Ads.objects.all()
#     return HttpResponse(f'{adv_res[adv_id]}')
#
#
# def categories_id(request, cat_id):
#     cat_res = Category.objects.all()
#     return HttpResponse(f'{cat_res[cat_id]}')
