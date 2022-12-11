from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Appointment(models.Model):
    class Meta:
        app_label = 'appointments'
        db_table = 'appointment'

    user = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField()
