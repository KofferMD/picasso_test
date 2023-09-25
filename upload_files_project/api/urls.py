from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import UploadViewSet, GetListFilesOrFile


router = DefaultRouter()
router.register(r'upload', UploadViewSet, basename='upload')
router.register(r'files', GetListFilesOrFile, basename='files')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
