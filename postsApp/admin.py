from django.contrib import admin

#my Models
from .models import Demo, ImageTest, Post,Comment, Test

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Test)
admin.site.register(Demo)
admin.site.register(ImageTest)

