from django.urls import  path
from .views import  list_pets, show_pet_details, like_pet

urlpatterns = [
    path('', list_pets, name='pet details'),
    path('details/<int:pk>', show_pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
]