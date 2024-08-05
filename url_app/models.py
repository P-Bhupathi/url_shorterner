from django.db import models

# Create your models here.
class Url_db(models.Model):
    source_url = models.URLField(max_length=10000)
    short_url = models.TextField(max_length=10,unique=True)
    valid_upto = models.TextField()
