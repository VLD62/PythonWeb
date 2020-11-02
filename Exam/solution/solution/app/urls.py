from django.urls import path
from .views.index import index
from .views.recepies import create_recepie, edit_recepie, delete_recepie, details_recepie


urlpatterns = (
    # Index
    path('', index, name='index'),
    # Actions
    path('create/', create_recepie, name='create recepie'),
    path('edit/<int:pk>/', edit_recepie, name='edit recepie'),
    path('delete/<int:pk>/', delete_recepie, name='delete recepie'),
    path('details/<int:pk>/', details_recepie, name='details recepie'),
)
