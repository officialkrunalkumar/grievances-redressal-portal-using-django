from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Complaint(models.Model):
    """
    This is the basic database for storing complaints.
    """
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=255, blank=True)
    user_type = (
        ('M', 'Mentor'),
        ('T', 'Trainee'),
    )
    user_role = models.CharField(
        max_length=1,
        choices=user_type,
        default='T',
    )
    date = models.DateTimeField(auto_now=True)
    complaint_type = (
        ('M', 'Management'),
        ('E', 'Education'),
        ('D', 'Deployment'),
        ('S', 'Salary'),
        ('G', 'General'),
    )
    complaint_for = models.CharField(
        max_length=1,
        choices=complaint_type,
        default='G',
    )
    complaint_type_to = (
        ('A', 'Admin'),
        ('M', 'Mentor'),
    )
    complaint_to = models.CharField(
        max_length=1,
        choices=complaint_type_to,
        default='M',
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
    complaint_category = (
        ('A', 'Anonymous'),
        ('I', 'Identifiable'),
    )
    category = models.CharField(
        max_length=1,
        choices=complaint_category,
        default='I',
    )
    complaint_status = (
        ('P', 'Pending'),
        ('N', 'Need Clarification'),
        ('R', 'Resolved'),
    )
    status = models.CharField(
        max_length=1,
        choices=complaint_status,
        default='P',
    )
    resoultion = models.TextField(blank=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)