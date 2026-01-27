from django.urls import path
from .views import HomePageView, AboutmeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutmeView.as_view(), name = 'about')
]