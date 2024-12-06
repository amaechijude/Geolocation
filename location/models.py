from django.db import models

# Create your models here.
class Location(models.Model):
    sch_name = models.TextField(blank=False)
    google_map = models.URLField(blank=False)

    def __str__(self):
        return f"{self.sch_name}"