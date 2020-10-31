from django.db import models
from django.db.models.signals import pre_save

from TechnicalRanjit.utils import unique_slug_generators


class BlogSection(models.Model):
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=5000, blank=True)
    description2 = models.TextField(max_length=5000, blank=True)
    description3 = models.TextField(max_length=5000, blank=True)
    image=models.CharField(max_length=1000,default="default.jpg",blank=True)
    link = models.CharField(max_length=1000, blank=True)


    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title




def rl_pre_save_receiverss(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(rl_pre_save_receiverss, sender=BlogSection)
