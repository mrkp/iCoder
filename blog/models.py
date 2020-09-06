from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=130)
    content = models.TextField()
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    created_at = models.DateTimeField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author