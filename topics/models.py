

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='topic_pics', default='default-post.jpg')
    content = HTMLField(blank=True, null=True)  
    published_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)
    is_featured = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title



class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = [ '-created']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.topic.title}'
