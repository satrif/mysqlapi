from django.contrib import admin
from .models import UserHierarchy, UserList, ArtList, ArtLikes, ArtCmt, Blog, BlogCmt, BlogLikes

# Register your models here.
admin.site.register(UserHierarchy)
admin.site.register(UserList)
admin.site.register(ArtList)
admin.site.register(ArtLikes)
admin.site.register(ArtCmt)
admin.site.register(Blog)
admin.site.register(BlogCmt)
admin.site.register(BlogLikes)

