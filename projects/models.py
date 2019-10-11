from django.db import models

class Project(models.Model):
    description = models.CharField(max_length=30)
    STATUS_CHOICES = [
        ('LATE', 'Late'),
        ('ON TRACK', 'On Track'),
        ('NEAR COMPLETIONS', 'Near Completion'),
    ]
    status = models.ChoiceField(choices = STATUS_CHOICES, default='ON TRACK')

class Milestone(models.Model):
    start = models.DateField()
    end = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Action(models.Model):
    description = models.CharField(max_length=300)
    status = models.BooleanField(default=False)
