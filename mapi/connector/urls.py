from django.conf.urls import url
from connector import views
# from .views import

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^UserHierarchy$', views.hierarchyApi),
                  url(r'^UserHierarchy/([0-9]+)$', views.hierarchyApi),
                  url(r'^UserList$', views.userApi),
                  url(r'^UserList/([0-9]+)$', views.userApi),
                  url(r'^ArtList$', views.artsApi),
                  url(r'^ArtList/([0-9]+)$', views.artsApi),
                  url(r'^ArtLikes$', views.artLikesApi),
                  url(r'^ArtLikes/([0-9]+)$', views.artLikesApi),
                  url(r'^ArtCmt$', views.artCmtApi),
                  url(r'^ArtCmt/([0-9]+)$', views.artCmtApi),
                  url(r'^Blog$', views.blogApi),
                  url(r'^Blog/([0-9]+)$', views.blogApi),
                  url(r'^BlogCmt$', views.blogCmtApi),
                  url(r'^BlogCmt/([0-9]+)$', views.blogCmtApi),
                  url(r'^BlogLikes$', views.blogLikesApi),
                  url(r'^BlogLikes/([0-9]+)$', views.blogLikesApi),
                  url(r'^Attachments/SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
