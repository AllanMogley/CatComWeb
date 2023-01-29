from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.memberList, name='List '),
    path('detail/<str:pk>/', views.memberDetail, name='Detail View '),
    path('create/', views.memberCreate, name='Create '),
    path('update/<str:pk>/', views.memberUpdate, name='Update '),
    path('delete/<str:pk>/', views.memberDelete, name='Delete '),
]
