from django.db import models
from django.db.models.enums import Choices


# Create your models here.
class complaints(models.Model):
    """
    This is the basic database for storing complaints.
    """
    title = models.CharField(max_length=200)
    complaint_type = (
        ('M', 'Management'),
        ('E', 'Education'),
        ('D', 'Deployment'),
        ('S', 'Salary'),
        ('G', 'General'),
    )
    complaint = models.CharField(
        max_length=1,
        choices=complaint_type,
        default='G',
    )
    cohort_choice = (
        ('P', 'Python'),
        ('J', 'Java'),
        ('R', 'React'),
        ('A', 'Android'),
        ('L', 'Linux'),
        ('C', 'Cybersecurity'),
        ('U', 'Unknown'),
    )
    cohort = models.CharField(
        max_length=1,
        choices=cohort_choice,
        default='U',
    )
    complaint_level = (
        ('I', 'Individual'),
        ('G', 'General'),
    )
    level = models.CharField(
        max_length=1,
        choices=complaint_level,
        default='I',
    )
    description = models.TextField(blank=False, max_length=500)
    status = models.IntegerField(default=0)
