from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    class Meta:
        verbose_name_plural = "Notes"

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, default="", on_delete=models.CASCADE)

    def _str_(self):
        return self.title
