from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)


class Project(models.Model):
    title = models.CharField(max_length=255)
    link_to_repository = models.CharField(max_length=255)
    user_set = models.TextField(blank=True)


class TODO(models.Model):
    notice = models.CharField(verbose_name='notice', max_length=255)
    notice_text = models.TextField(verbose_name='notice_text', blank=True)
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    author = models.CharField(verbose_name='author', max_length=255)
    fk = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
