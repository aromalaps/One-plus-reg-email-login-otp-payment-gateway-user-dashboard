from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import OTP

@shared_task
def delete_expired_otps():
    expiration_time = timezone.now() - timedelta(minutes=10)
    OTP.objects.filter(created_at__lt=expiration_time).delete()
