from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    do_in = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todolist')

    class Meta:
        ordering = ('do_in',)

    def __str__(self):
        return self.task
