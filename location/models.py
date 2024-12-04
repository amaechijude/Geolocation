from django.db import models

# Create your models here.
class School(models.Model):
    sch_name = models.CharField(blank=False, max_length=25)
    google_map = models.URLField()

    def __str__(self):
        return f"{self.sch_name}"