"""djangular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from graphene_django.views import GraphQLView
from books.schema import schema
from django.views.decorators.csrf import csrf_exempt

from jaksiemieszka.views import UserViews, ExampleView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('jaksiemieszka.urls')),
    path('api/token/', csrf_exempt(jwt_views.TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/', csrf_exempt(jwt_views.TokenRefreshView.as_view()), name='token_refresh'),
    path('api/user/', csrf_exempt(ExampleView.as_view()), name='user'),


    path("books/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    url(r'^.*', TemplateView.as_view(template_name="index.html"), name='home'),
]
