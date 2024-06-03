from django.db import models
import assignments
from courses.models import Course
from django.utils.html import format_html

# Create your models here.
class Assignment(models.Model):
    unique_name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length = 250)
    questions = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.topic
    

class Submission(models.Model):
    user = models.CharField(max_length=250)
    file = models.FileField(upload_to = 'media')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return "Submission by " + self.user
    

