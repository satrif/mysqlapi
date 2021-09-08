from rest_framework import serializers
from connector.models import UserHierarchy, UserList, ArtList, ArtLikes, ArtCmt, Blog, BlogCmt, BlogLikes


class UserHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHierarchy
        fields = ('UH_ID', 'UH_Name')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ('UL_ID', 'UL_Login', 'UL_Pass', 'UL_Name', 'UL_Email', 'UL_Confirmed')


class ArtListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtList
        fields = ('AL_ID', 'AL_Name', 'AL_AddDate', 'AL_Artist', 'AL_ArtPath')


class ArtLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtLikes
        fields = ('ALi_ID', 'ALi_Item', 'ALi_User')


class ArtCmtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtCmt
        fields = ('AC_ID', 'AC_User', 'AC_Text', 'AC_Date')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('B_ID', 'B_Title', 'B_Date', 'B_Text', 'B_Pics', 'B_UserName', 'B_Login')


class BlogCmtSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCmt
        fields = ('BC_ID', 'BC_B_ID', 'BC_User', 'BC_Text', 'BC_Date')


class BlogLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLikes
        fields = ('BL_ID', 'BL_Item', 'BL_User')


