from django.urls import path
from .views import HomePageView,AboutPageView,GamePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about.html'),
    path('', HomePageView.as_view(), name='home.html'),
    path('game/', GamePageView.as_view(), name='game.html'),

]