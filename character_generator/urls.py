from django.urls import path
from .views import GenerateCharacterView

urlpatterns = [
    path('generate/', GenerateCharacterView.as_view(), name='generate_character'),
]