from django.db import models

# Create your models here.
class Log(models.Model):
    msg_type = [
        ('Warning', 'Warning'),
        ('Print', 'Print'),
        ('Error', 'Error'),
        ('Confirm', 'Confirm'),
        ('OK', 'OK')
    ]
    created_at = models.DateTimeField(auto_now=True, editable=True)
    msg = models.TextField(null=True)
    type = models.CharField(
        max_length=20,
        choices=msg_type,
        default='OK'
    )

    def __str__(self) -> str:
        return self.type + " - " + self.msg
