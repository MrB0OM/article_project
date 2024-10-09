from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=221)
    job = models.CharField(max_length=211)
    image = models.ImageField(upload_to="feedback/")
    comment = models.TextField()

    def __str__(self):
        return self.full_name