from django.urls import path
from . import views

urlpatterns = [
    path('member-list/', views.memberList, name='List '),
    path('member-detail/<str:pk>/', views.memberDetail, name='Detail View '),
    path('member-create/', views.memberCreate, name='Create '),
    path('member-update/<str:pk>/', views.memberUpdate, name='Update '),
    path('member-delete/<str:pk>/', views.memberDelete, name='Delete '),
]
