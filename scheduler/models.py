from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    batch = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='lectures')
    date = models.DateField()

    class Meta:
        unique_together = ('instructor', 'date')
    
    def __str__(self):
        return f"{self.course.name} - {self.date} by {self.instructor.name}"
