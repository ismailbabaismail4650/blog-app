from django.urls import path
from . views import HomeView,PostDetailView,AddPostView,EditPostView,DeletePostView,AddCategoryView,CategoryView,LikeView,AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_categoy/', AddCategoryView.as_view(), name="add_category"),
    path('edit/<int:pk>', EditPostView.as_view(), name="edit"),
    path('delete/<int:pk>', DeletePostView.as_view(), name="delete"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name = 'like'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="comment"),
     
]
