from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    # Delete url
    path('delete/<int:blog_id>', views.delete, name="delete"),
    # Update url
    path('update/<int:blog_id>', views.update, name="update"),
    path('updateSend/<int:blog_id>', views.updateSend, name="updateSend"),
    path('newblog/', views.blogpost, name="newblog"),
]