from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet,
    signup,
    token,
)

app_name = 'api'

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='login'),
    path('v1/auth/code/', signup, name='code'),
]
