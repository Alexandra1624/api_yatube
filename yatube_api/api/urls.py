from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import GroupsViewSet, CommentsViewSet, PostsViewSet, FollowsViewSet


router = DefaultRouter()
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'groups', GroupsViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')
router.register(r'follow', FollowsViewSet, basename='follows')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
