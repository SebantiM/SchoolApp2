from django.urls import path, include
from . import views

app_name = 'physics'
urlpatterns = [
    path('grade12', views.g12home, name = 'g12home'),
    path('grade12/reading', views.reading, name = 'reading')
]