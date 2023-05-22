from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns=[
    # path('',views.home,name='blog-home'),
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about')

]


# class based view--  template pattern
# blog/post_list.html -- <app_name> / <model_name> _ <class view type> . html