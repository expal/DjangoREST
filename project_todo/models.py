from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    link_to_repository = models.CharField(max_length=255)
    user_set = models.TextField(blank=True)


class TODO(models.Model):
    notice = models.CharField(max_length=255)
    notice_text = models.TextField(blank=True)
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    author = models.CharField(max_length=255)
    fk = models.ForeignKey(Project)
    is_active = models.BooleanField(default=True)
