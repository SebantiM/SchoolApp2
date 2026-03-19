from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
     path('', views.home, name = 'home'),
     path('home/grade12', views.grade12index, name = 'grade12index'),
     #path('grade12/Scinece/index',views.garde12SciecneIndex, name='grade12SciecneIndex' ),
]
