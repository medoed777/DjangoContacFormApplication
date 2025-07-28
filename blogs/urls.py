from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blogs.views import (
    BlogsListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogDetailView,
)

app_name = "blogs"

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
