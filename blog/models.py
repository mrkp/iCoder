from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=130)
    content = models.TextField()
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_image')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 
class BlogComment(models.Model):

    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15] + "... " + "by - " + self.user.username