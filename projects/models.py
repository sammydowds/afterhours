from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('LATE', 'Late'),
        ('ON TRACK', 'On Track'),
        ('NEAR COMPLETIONS', 'Near Completion'),
    ]
    description = models.CharField(max_length=30)
    status = models.CharField(choices = STATUS_CHOICES, default='ON TRACK', max_length=20)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)

class Milestone(models.Model):
    start = models.DateField()
    end = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Action(models.Model):
    description = models.CharField(max_length=300)
    status = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
