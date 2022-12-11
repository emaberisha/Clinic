from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.

class Doctor(models.Model):
    class Meta:
        app_label = 'users'
        db_table = 'doctor'

    user = models.ForeignKey(User, related_name='doctors', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class UserDoctor(models.Model):
    class Meta:
        app_label = 'users'
        db_table = 'user_doctor'
        unique_together = ('user_id', 'doctor_id')

    user = models.ForeignKey(User, related_name='user_doctors', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, related_name='user_doctors', on_delete=models.CASCADE, null=True)
