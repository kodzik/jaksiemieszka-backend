from django.contrib import admin
from jaksiemieszka.models import Comment, CommentRating
# from jaksiemieszka.models import User

# Register your models here.
# admin.site.register(User)
admin.site.register(CommentRating)
admin.site.register(Comment)
