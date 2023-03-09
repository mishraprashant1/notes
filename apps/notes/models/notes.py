from django.db import models
from django.contrib.auth.models import User

import uuid


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)
    deleted_on = models.DateTimeField(null=True)
    uuid = models.UUIDField(default = uuid.uuid4, null=True)
