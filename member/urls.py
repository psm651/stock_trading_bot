from django.urls import path

from . import views
print('members url', views.index)
urlpatterns = [
    path('', views.index, name='index'),
]
