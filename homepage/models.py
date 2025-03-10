from termios import TIOCSER_TEMT

from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete= models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.title