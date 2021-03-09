from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class BlogPostCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(default=datetime.now, blank=True)
    post_category = models.ManyToManyField(BlogPostCategory)
    post_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
