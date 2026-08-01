from django.urls import path
from urllib import request
from .views import HomePageView
from .views import HomePageView1, RadioView, status_view

urlpatterns = [
    path("xxx/", HomePageView.as_view(), name="home"),
    path("", HomePageView1, name="home1"),
    path("radio/", RadioView, name="radio"),
    path("status/", status_view, name="status"),
]
