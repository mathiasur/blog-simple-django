from django.urls import path
from .views import BlogListView, PostCreateView, PostDetailView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update')
]


