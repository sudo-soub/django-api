from django.dispatch import receiver
from tutorials.models import Tutorial
from django.db.models.signals import pre_save, post_save


@receiver(pre_save, sender=Tutorial)
def beforesaving(instance, **kwargs):
    print("This signal is called pre save")


@receiver(post_save, sender=Tutorial)
def aftersaving(instance, **kwargs):
    print("This signal is called after saving")
