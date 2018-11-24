from django.urls import path
from . import views

urlpatterns = [
    path('/chitchatmodel', views.chitchatmodel, name='chitchatmodel'),
    path('/taskedchatbot', views.taskedchatbot, name='taskedchatbot'),
    path('/FAQ', views.faq, name='faq'),
]
