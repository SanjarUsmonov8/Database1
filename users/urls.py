from django.urls import path
from .views import MahsulotAPI


urlpatterns = [
    path('mahsulot', MahsulotAPI.as_view())
]