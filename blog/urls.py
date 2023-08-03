from django.urls import path
from .views import BlogListView, PostCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create')
]


