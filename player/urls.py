from django.urls import path
from .views import signup, HomePageView, AboutPageView, CreationPageView

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('create-character/', CreationPageView.as_view(), name='create-character'),

]
