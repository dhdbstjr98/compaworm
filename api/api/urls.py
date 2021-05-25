from django.urls import path
from . import views

urlpatterns = [path('user/me', views.UserMe.as_view())]
