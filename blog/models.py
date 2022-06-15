from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.html import format_html
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    views = models.IntegerField(default=0)
    content=models.TextField()
    image = models.ImageField(upload_to='media', default="")

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

# Models for videos

class Video(models.Model):
    sno = models.AutoField(primary_key = True)
    caption = models.CharField(max_length = 100)
    speaker = models.CharField(max_length = 100, default = "")
    video = models.FileField(upload_to= 'media')
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.caption



