from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from api.serializers import FileSerializer
from uploader.models import File
from api.tasks import set_processed

class CreateFileViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    pass


class GetListOrGetOnlyOneFileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class UploadViewSet(CreateFileViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        set_processed.delay(instance.id)
        return instance


class GetListFilesOrFile(GetListOrGetOnlyOneFileViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
