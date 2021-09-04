from rest_framework import routers
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'posts', PostViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register(r'follow', FollowViewSet, basename='follow')

v1_patterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(v1_patterns)),
]
