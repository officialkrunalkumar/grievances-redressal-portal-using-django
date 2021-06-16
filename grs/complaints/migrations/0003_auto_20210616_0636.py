# Generated by Django 3.2.4 on 2021-06-16 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0002_rename_complaints_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint',
            new_name='complaint_for',
        ),
        migrations.AddField(
            model_name='complaint',
            name='category',
            field=models.CharField(choices=[('A', 'Anonymous'), ('I', 'Identifiable')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_to',
            field=models.CharField(choices=[('A', 'Admin'), ('M', 'Mentor')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='user_role',
            field=models.CharField(choices=[('M', 'Mentor'), ('T', 'Trainee')], default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('N', 'Need Clarification'), ('R', 'Resolved')], default='P', max_length=1),
        ),
    ]
