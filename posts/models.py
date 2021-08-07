from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.TimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'id': self.id})
