from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
