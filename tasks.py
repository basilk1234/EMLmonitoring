# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .models import EmergencyLight

@shared_task
def check_emergency_lights():
    emergency_lights = EmergencyLight.objects.all()
    for emergency_light in emergency_lights:
        if emergency_light.battery_level < 20:
            send_mail(
                'Emergency Light Alert',
                f'The emergency light {emergency_light.name} at {emergency_light.location} has a low battery level of {emergency_light.battery_level}%. Please check and replace the battery as needed.',
                'noreply@yourdomain.com',
                ['admin@yourdomain.com'],
                fail_silently=False,
            )
