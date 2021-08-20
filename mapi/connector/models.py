from django.db import models


# Create your models here.
# from django.db.models import Count
# User.objects.aggregate(Count('id'))
class UserHierarchy(models.Model):
    UH_ID = models.AutoField(primary_key=True)
    UH_Name = models.CharField(max_length=20, verbose_name='Family Role')

    def __str__(self):
        return self.UH_Name

    class Meta:
        verbose_name = 'Hierarchy'
        verbose_name_plural = 'Hierarchy'


class UserList(models.Model):
    UL_ID = models.AutoField(primary_key=True)
    UL_Login = models.CharField(max_length=20, unique=True, verbose_name='Login')
    UL_Pass = models.CharField(max_length=20, verbose_name='Pass')
    UL_Name = models.CharField(max_length=20, unique=True, verbose_name='Name')
    # UL_SName = models.CharField(max_length=20, verbose_name='Surname')
    # UL_Age = models.IntegerField()
    UL_Email = models.CharField(max_length=50, verbose_name='eMail')
    UL_H = models.ForeignKey(UserHierarchy, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Family Role')
    UL_Confirmed = models.BooleanField(default=False, verbose_name='Confirmed')

    def __str__(self):
        return self.UL_Name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ArtList(models.Model):
    AL_ID = models.AutoField(primary_key=True)
    AL_Name = models.CharField(max_length=50, verbose_name='Art Name')
    AL_AddDate = models.DateTimeField(auto_now=True, verbose_name='Date Add')
    AL_Artist = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Artist')
    AL_ArtPath = models.TextField(verbose_name='Path to Art')

    def __str__(self):
        return self.AL_Name

    class Meta:
        verbose_name = 'Art'
        verbose_name_plural = 'Arts'


class ArtLikes(models.Model):
    ALi_ID = models.AutoField(primary_key=True)
    ALi_Item = models.ForeignKey(ArtList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Art Name')
    ALi_User = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Art Liker')

    def __str__(self):
        return self.ALi_ID

    class Meta:
        verbose_name = 'Art Like'
        verbose_name_plural = 'Art Likes'


class ArtCmt(models.Model):
    AC_ID = models.AutoField(primary_key=True)
    AC_User = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Art Commenter')
    AC_Text = models.TextField(verbose_name='Comment Text')
    AC_Date = models.DateTimeField(auto_now=True, verbose_name='Comment Date')

    def __str__(self):
        return self.AC_Text

    class Meta:
        verbose_name = 'Art Comment'
        verbose_name_plural = 'Art Comments'


class Blog(models.Model):
    B_ID = models.AutoField(primary_key=True)
    B_Title = models.CharField(max_length=50, verbose_name='Blog Title')
    B_User = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Blogger')
    B_Date = models.DateTimeField(auto_now=True, verbose_name='Blog Post Date')
    B_Text = models.TextField(verbose_name='Blog Text')
    B_Pics = models.TextField(verbose_name='Blog Media')

    def PicList(self):
        return str(self.B_Pics).split(sep=" ")

    def __str__(self):
        return self.B_Title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class BlogCmt(models.Model):
    BC_ID = models.AutoField(primary_key=True)
    BC_B_ID = models.ForeignKey(Blog, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Blog Comment')
    BC_User = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Blog Commenter')
    BC_Text = models.TextField(verbose_name='Blog Comment Text')
    BC_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.BC_Text

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'


class BlogLikes(models.Model):
    BL_ID = models.AutoField(primary_key=True)
    BL_Item = models.ForeignKey(Blog, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Blog')
    BL_User = models.ForeignKey(UserList, on_delete=models.PROTECT, null=True, blank=True, verbose_name='User')

    def __str__(self):
        return self.BL_ID

    class Meta:
        verbose_name = 'Blog Like'
        verbose_name_plural = 'Blog Likes'





