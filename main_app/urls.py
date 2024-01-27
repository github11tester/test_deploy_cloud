from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasePageView.as_view())
]