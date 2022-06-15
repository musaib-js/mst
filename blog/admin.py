from django.contrib import admin
from .models import Post
from .models import BlogComment, Video
from django.utils.html import format_html

admin.site.register((BlogComment, Video))
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)