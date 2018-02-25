from django.db import models


class Main(models.Model):
    text = models.TextField(max_length=400)
    is_deleted = models.BooleanField(default=False)
