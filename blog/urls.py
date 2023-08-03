from django.urls import path
from .views import BlogListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete')
]


