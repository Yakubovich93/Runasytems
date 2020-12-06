from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children'
    )
    def __str__(self):
        return self.name

