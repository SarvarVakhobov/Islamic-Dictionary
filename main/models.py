from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Words(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='word_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title
