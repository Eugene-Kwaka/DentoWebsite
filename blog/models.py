from django.db import models
from django.urls import reverse
from tinymce import HTMLField
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
#from dentist.models import Patient

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    #profile_picture = models.ImageField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id,
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id,
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id,
        })

# this method is for the indivdual comments for a blogpost that are shown in the order of newest to oldest comment
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

# This method is for the comment count that shows number of comments per blogpost
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
