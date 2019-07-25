from django.db import models

# Create your models here.
class FilePost(models.Model):
    username = models.CharField(max_length=30)
    text = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()

    # def __str__(self):
    #     return self.username + ' said ' + self.text
