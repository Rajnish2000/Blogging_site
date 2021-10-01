from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=60,default="")
    title = models.CharField(max_length=100,default="")
    content = models.TextField()
    slug = models.CharField(max_length=120)
    timestamp = models.DateField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.TimeField(default=now)

    def __str__(self):
        return self.comment[0:12] + " by " + self.user.username
        