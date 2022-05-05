from django.urls import path
from .views import CommentViews
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('comments/', csrf_exempt(CommentViews.as_view()) ),
]