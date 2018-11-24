from django.urls import path
from . import views

urlpatterns = [
    path('/Stuttgart', views.index, name='index'),
    path('', views.sentiment, name='sentiment'),
]
