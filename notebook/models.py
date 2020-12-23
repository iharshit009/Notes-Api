from django.db import models


class Notes(models.Model):
    class Meta:
        verbose_name_plural = "Notes"

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def _str_(self):
        return self.title
