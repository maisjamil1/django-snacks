from .views import HomeView, AboutView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'), # 3
    path('about', AboutView.as_view(), name='about'),
]