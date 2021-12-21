from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article.views import CommentViewSet, ArticleViewset
from courses.views import CourseViewSet
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('article', ArticleViewset)
router.register('comment', CommentViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include('user.urls')),
    path('api/v2/', include('video.urls')),
    path('api/v2/', include(router.urls)),
    path('api/v2/', include('courses.urls')),
    path('api/v1/', include('package.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
