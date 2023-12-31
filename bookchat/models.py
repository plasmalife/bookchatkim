from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50, null=False) 
    book_cover = models.ImageField(upload_to='img')
    file = models.FileField(upload_to='pdf')
    intro = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=20, null=False)
    author_intro = models.CharField(max_length=200, null=False)
    pickle = models.FileField(upload_to='pickle', blank=True)

    def __str__(self):
        return f"{self.title} ({self.author})"

class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.CharField(max_length=50)
    user_msg = models.CharField(max_length=400)
    bot_msg = models.CharField(max_length=400)
    def __str__(self):
        return f"{self.book} ({self.user})"