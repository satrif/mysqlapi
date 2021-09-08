from django.contrib import admin
from .models import UserHierarchy, UserList, ArtList, ArtLikes, ArtCmt, Blog, BlogCmt, BlogLikes


# Register your models here.
class Users(admin.ModelAdmin):
    list_display = ('UL_Login', 'UL_Pass', 'UL_Name', 'UL_Email', 'UL_Confirmed')
    list_display_links = ('UL_Login', 'UL_Name')
    search_fields = ('UL_Login', 'UL_Pass', 'UL_Name', 'UL_Email')
    # list_filter = ('orderStatus',)
    # list_editable = ('orderStatus', 'orderPhone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('UL_Login', 'UL_Pass', 'UL_Name', 'UL_Email', 'UL_Confirmed')
    # readonly_fields = ('id', 'orderDate')


admin.site.register(UserHierarchy)
admin.site.register(UserList, Users)
admin.site.register(ArtList)
admin.site.register(ArtLikes)
admin.site.register(ArtCmt)
admin.site.register(Blog)
admin.site.register(BlogCmt)
admin.site.register(BlogLikes)
