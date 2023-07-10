from django.urls import path
from .views import bookmark_list_viewer

urlpatterns = [
    path('', bookmark_list_viewer, name='bookmarkList'),
]