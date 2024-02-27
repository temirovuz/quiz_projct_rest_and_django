from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

STATUS_CHOICES = (
    ('new', 'new'),
    ('prosessing', 'prosessing'),
    ('finished', 'finished'),
)


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='new')

    def __str__(self):
        return self.title


@receiver(post_save, sender=Task)
def change_status(sender, instance, **kwargs):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('check_status', {
        "type": "get_status",
        "data": {
            'test': "status change",
            'pk': instance.pk,
            'status': instance.status,
        }
    })
