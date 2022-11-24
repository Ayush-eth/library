from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('',views.library,name='library')
    # path('library',views.library,name='library')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)