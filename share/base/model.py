from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)

    class Meta:
        abstract = True
