from django.contrib import admin
from .models import Post, Category, Tag, Comment, PostPhoto, Subscription

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(PostPhoto)
admin.site.register(Subscription)


