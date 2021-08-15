from django.urls import path, include
from srtvShow import views

urlpatterns = [
    path('', views.index),
    path('shows/', include('srtvShow.urls')),
]
