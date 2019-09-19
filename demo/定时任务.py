import datetime

from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import default_storage


@shared_task



def demo():
    pass