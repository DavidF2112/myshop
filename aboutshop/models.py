from django.db import models

class Aboutshop(models.Model):
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=50)


    class Meta:
        ordering = ('name',)
        verbose_name = 'service'
        verbose_name_plural = 'services'