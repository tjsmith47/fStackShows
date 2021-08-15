from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #localhost:8000/
    path('new', views.new), #localhost:8000/shows/new
    path('reset', views.reset), #localhost:8000/shows/reset
    path('create', views.create), #localhost:8000/shows/create
    path('<int:show_id>', views.display), #localhost:8000/shows/1
    path('<int:show_id>/edit', views.edit), #localhost:8000/shows/1/edit
    path('<int:show_id>/update', views.update), #localhost:8000/shows/1/update
    path('<int:show_id>/destroy', views.destroy), #localhost:8000/shows/1/destroy
]