from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    name = models.CharField(max_length=255)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Task for {self.user.username} - {self.app.name}'

class Screenshot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='screenshots/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Screenshot by {self.user.username} for {self.app.name}'
