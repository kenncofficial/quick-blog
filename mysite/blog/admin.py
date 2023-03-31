from django.contrib import admin
from .models import BlogPost, Category, BlogComment, WriterProfile, About, Roles
# Register your models here.

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(WriterProfile)
admin.site.register(About)
admin.site.register(Roles)