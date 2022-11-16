from django.conf.urls.static import static
from django.urls import path, re_path

from djangoHomework1 import settings
from .views import *

urlpatterns = [
    path('', index),
    path('ad/', AdsView.as_view()),
    path('cat/', CatView.as_view()),
    path('ad/<int:pk>/', AdsDetailView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = pageNotFound