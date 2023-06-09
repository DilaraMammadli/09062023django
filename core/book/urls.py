from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name="index"),
    path('create/', views.create_view, name="create"),
    path('list/', views.list_view, name="list"),
    path('detail/<id>/', views.detail_view, name="detail"),
]


