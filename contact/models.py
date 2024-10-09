from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.CharField()
    subject = models.CharField(max_length=221)
    comment = models.TextField

class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=211)
    comment = models.TextField()

    def __str__(self):
        return self.name