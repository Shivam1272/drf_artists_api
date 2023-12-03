from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from artist.views import CustomUserCreate, WorkViewSet, ArtistViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'works', WorkViewSet, basename='work')
router.register(r'artists', ArtistViewSet, basename='artist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', CustomUserCreate.as_view(), name='user_register'),
    path('api/token/', ObtainAuthToken.as_view(), name='token_obtain'),
    path('api/', include(router.urls)),
]
