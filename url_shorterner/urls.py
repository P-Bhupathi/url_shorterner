
from django.contrib import admin
from django.urls import path
from url_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('sort_url',sort_url,name='sort_url'),
    path('short/<str:id>',short,name='short')
]
