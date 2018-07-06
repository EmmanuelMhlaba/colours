from django.conf.urls import re_path

from colours import views

app_name = 'colours'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
]