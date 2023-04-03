from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import CustomUserViewSet, ProfileViewSet
from api.views import logout

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('logout/', logout, name='logout'),
]

#  path('myself/', ManageUserView.as_view(), name='myself'),

