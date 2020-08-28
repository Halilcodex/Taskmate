from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    # user = models.ForeignKey(User, blank=True, null=True, related_name="task_user", on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ('-created_date',)