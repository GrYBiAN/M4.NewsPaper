from django.urls import path
from .views import PostsList, PostDetail, Search, PostEdit, PostDelete, PostCreate, CreateAR, subscriptions

urlpatterns = [
    path('', PostsList.as_view(), name=''),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', Search.as_view()),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/del/', PostDelete.as_view(), name='post_delete'),
    path('create/', PostCreate.as_view(), name ='post_create'),
    path('articles/create/', CreateAR.as_view(), name='article_create'),
    path('articles/<int:pk>/del/', PostDelete.as_view(), name='article_delete'),
    path('articles/<int:pk>/edit/', PostEdit.as_view(), name='article_edit'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]