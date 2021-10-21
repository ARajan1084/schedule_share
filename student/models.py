import uuid

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'students'


class Class(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    course_name = models.CharField(max_length=50, null=False)
    teacher_first_name = models.CharField(max_length=30, null=False)
    teacher_last_name = models.CharField(max_length=50, null=False)
    # sunday = 0
    day = models.IntegerField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    class Meta:
        db_table = 'classes'


class Friendship(models.Model):
    a = 1
    # TODO: finish


class FriendRequest(models.Model):
    a = 1
    # TODO: finish


class Enrollment(models.Model):
    a = 1
    # TODO: finish