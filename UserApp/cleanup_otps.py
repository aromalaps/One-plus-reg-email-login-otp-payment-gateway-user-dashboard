
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from .models import OTP

class Command(BaseCommand):
    help = 'Delete expired OTPs'

    def handle(self, *args, **kwargs):
        expiration_time = timezone.now() - timedelta(minutes=10)
        expired_otps = OTP.objects.filter(created_at__lt=expiration_time)
        count, _ = expired_otps.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired OTPs'))
