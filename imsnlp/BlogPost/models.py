from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    time_created = models.DateTimeField('date published')

    def __str__(self):
        return "Title:\n"+self.title + "\nContent:\n" +self.content + "\nCreated: "+self.time_created
