from django.urls import path
from . import views

#make media file accessable
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.getRoutes,name="routes"),
    path("posts",views.AllPosts.as_view(),name="allPosts"),
    path("post/<str:pk>",views.UpdatePost.as_view(),name="updatePost"),
    path("test/<str:pk>",views.getTestData,name="testdata"),
    path("images",views.ImageView.as_view(),name="images"),
    path("image/<str:pk>",views.ImageUpdate.as_view(),name="imageUpdate")
]

#make media file accessable
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
