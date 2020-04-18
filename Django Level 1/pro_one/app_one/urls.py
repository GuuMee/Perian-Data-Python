from django.conf.urls import url
from app_one import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]
