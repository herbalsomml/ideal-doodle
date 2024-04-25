from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import SiteSettings


@receiver(post_save, sender=SiteSettings)
def create_or_update_settings(sender, instance, created, **kwargs):
    if created:
        SiteSettings.objects.exclude(pk=instance.pk).delete()
