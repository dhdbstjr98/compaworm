from django.urls import path
from . import views

urlpatterns = [
    path("user/me", views.UserMeView.as_view()),
    path("comparison/<str:obj1>/<str:obj2>", views.ComparisonView.as_view()),
    path("comment/<str:obj1>/<str:obj2>", views.CommentView.as_view()),
]
