from django.urls import path
from .views import HomePageView, AboutPageView, Market,Baha

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('market/', Market.as_view(), name='m'),
    path('baha/', Baha.as_view(), name='ba'),
]