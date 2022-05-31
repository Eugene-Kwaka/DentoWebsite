from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="post-list"),
    path('post/<id>/', views.post, name="post-detail"),
    path('create/', views.post_create, name="post-create"),
    path('post/<id>/update/', views.post_update, name="post-update"),
    path('post/<id>/delete/', views.post_delete, name="post-delete"),
    path('categories', views.categories, name="categories"),
    path('add_category/', views.add_category, name="add_category"),
    path('update_category/<int:pk>/', views.update_category, name="update_category"),
    path('delete_category/<int:pk>/,', views.delete_category, name="delete_category"),
    path('search/', views.search, name="search"),
]
