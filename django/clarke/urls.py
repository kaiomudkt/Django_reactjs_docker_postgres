from django.contrib import admin
from django.urls import path
from clarke.views import teste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste)
]
