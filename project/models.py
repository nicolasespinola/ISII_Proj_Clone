from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    projectName = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField()
    ##sprints = models.ArrayField(models.IntegerField())
    status = models.CharField(max_length=50)
    ##actualSprint = models.IntegerField()
    lead = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectName


class ProjectPermit(models.Model):
    name = models.CharField(max_length=50)
    permitDescription = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    roleDescription = models.CharField(max_length=50)
    projectPermit = models.ManyToManyField(ProjectPermit)

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    def __str__(self):
        return self.userId.username
