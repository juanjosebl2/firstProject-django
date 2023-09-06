from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    #Para visulizar el nombre y no solo se vea un objeto
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Relation
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + " - " + self.project.name