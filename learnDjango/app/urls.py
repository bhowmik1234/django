from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_app, name='all_home'),
    path('store/', views.store, name='store'),
    path('<int:id>/', views.desp, name='desp'),
]
