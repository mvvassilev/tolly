from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('storage/', views.storage, name='storage'),
    path('regitems/', views.regitems, name='regitems'),
    path('add_item', views.add_item)
]