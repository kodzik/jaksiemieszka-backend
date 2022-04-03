from django.urls import path
from .views import UserViews, CommentViews
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users/', csrf_exempt(UserViews.as_view()) ),
    path('comments/', csrf_exempt(CommentViews.as_view()) ),
]