from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

class Project(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-id']