from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('school', 'School'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    linked_student_id = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.username} ({self.role})"
    
class StudentAchievement(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    school_name = models.CharField(max_length=255)
    achievements = models.TextField()

    def __str__(self):
        return f"{self.student.username} - {self.achievements}"