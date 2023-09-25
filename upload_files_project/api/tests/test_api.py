import tempfile

from http import HTTPStatus
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from PIL import Image

from uploader.models import File


class TestAPI(APITestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        file_content = b'test_file_content'
        file_content1 = b'test_file_content'

        cls.test_file = SimpleUploadedFile('test_file.txt', file_content)
        cls.test_file1 = SimpleUploadedFile('test_file.txt', file_content1)

        cls.file = File.objects.create(file=cls.test_file)
        cls.file1 = File.objects.create(file=cls.test_file1)


    def test_get(self):
        urls = (
            ('files-list', None),
            ('files-detail', (self.file.id,)),
        )

        for name, args in urls:
            with self.subTest(name=name):
                url=reverse(name, args=args)
                respose = self.client.get(url)
                self.assertEqual(respose.status_code, HTTPStatus.OK)


    def test_post(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        url = reverse('upload-list')
        response = self.client.post(
            url,
            {'image': tmp_file},
            format='multipart'
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED
        )

