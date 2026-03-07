from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница
    path('', views.PostListView.as_view(), name='index'),

    # Страница поста
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),

    # Создание поста
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),

    # Редактирование поста
    path(
        'posts/<int:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),

    # Удаление поста
    path(
        'posts/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),

    # Комментарии
    path(
        'posts/<int:pk>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path('posts/<int:post_id>/edit_comment/<int:pk>/',
         views.CommentUpdateView.as_view(), name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:pk>/',
         views.CommentDeleteView.as_view(), name='delete_comment'),

    # Категории
    path('category/<slug:category_slug>/',
         views.CategoryPostsView.as_view(), name='category_posts'),

    # Профиль пользователя
    path(
        'profile/<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
