from django.contrib import admin

from .models import IdeaPost
from .models import Comment

admin.site.register(IdeaPost)
admin.site.register(Comment)

# Register your models here.
