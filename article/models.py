from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_date = models.DateField(auto_now_add=True)  # Sana avtomatik qo'shiladi
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Mail(models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail
