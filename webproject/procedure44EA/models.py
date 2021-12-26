from django.db import models

class Procedurestatus(models.Model):
    code = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedureStatus'