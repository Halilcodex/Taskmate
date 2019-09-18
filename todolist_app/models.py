from django.db import models

# Create your models here.

class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ('-created_date',)