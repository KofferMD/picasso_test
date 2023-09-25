from celery import shared_task
from uploader.models import File


@shared_task
def set_processed(file_id):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
    except File.DoesNotExist:
        return False
    except Exception as e:
        return str(e)