from django.urls import path
from .views import UserViews, CommentViews, HelloView
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('users/', csrf_exempt(UserViews.as_view()) ),
    path('comments/', csrf_exempt(CommentViews.as_view()) ),
    path('hello/', csrf_exempt(HelloView.as_view()) ),
]