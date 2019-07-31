from django.db import models
from django.contrib.postgres.fields import JSONField

# Route Model
class Route(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  # Using JSONfield to make it easier to store path data as an array of obj with text and decimal ints
  path = JSONField()
  owner = models.ForeignKey('auth.User', related_name='routes', on_delete=models.CASCADE, null=True)

  # save route to owner
  def save(self, *args, **kwargs):
    super(Route, self).save(*args, **kwargs)

