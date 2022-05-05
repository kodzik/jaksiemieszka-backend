from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views
from . import views

# from rest_framework import routers
# from .views import UserViewSet
# from django.conf.urls import url, include

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    # url(r'^', include(router.urls)),
    # path('', include(router.urls)),
    # path('auth/', include('rest_auth.urls')),


    path('token/', csrf_exempt(jwt_views.TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('token/refresh/', csrf_exempt(jwt_views.TokenRefreshView.as_view()), name='token_refresh'),
    path('user/', csrf_exempt(views.UserView.as_view()), name='user'),
    path('register/', csrf_exempt(views.RegisterView.as_view()), name='auth_register'),

]