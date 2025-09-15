from datetime import time
from django.db import models
from django.utils import timezone


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(TimeStampMixin):
    COURSES_CHOICES = (
        ("python","python"),
        ("django","django"),
        ("javascript","javascript"),
        ("html","html"),
        ("react.js","react.js"),
        ("scratch","scratch"),
    )
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    referrer_name = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=15, choices=COURSES_CHOICES)
    # classs

    def __str__(self):
        return f"{self.full_name}"


class Class(TimeStampMixin):
    student = models.OneToOneField(
        to=Student, on_delete=models.PROTECT, related_name="classs"
    )
    class_link = models.URLField()
    upload_link = models.URLField(blank=True, null=True)
    # times

    def __str__(self):
        return f"{self.student.full_name}"


class ClassTime(TimeStampMixin):
    CHOICES = (
        (1, "شنبه"),
        (2, "یکشنبه"),
        (3, "دوشنبه"),
        (4, "سه شنبه"),
        (5, "چهارشنبه"),
        (6, "پنجشنبه"),
        (7, "جمعه"),
    )
    weekday = models.IntegerField(choices=CHOICES)
    start_time = models.TimeField(default=time(10, 0, 0))
    end_time = models.TimeField(default=time(11, 0, 0))
    classs = models.ForeignKey(to=Class, on_delete=models.CASCADE, related_name="times")
    # sessions

    def __str__(self):
        return f"{self.get_weekday_display()} {str(self.start_time)[:5]} {self.classs.student}"

class Session(TimeStampMixin):
    class_time = models.ForeignKey(to=ClassTime, on_delete=models.PROTECT, related_name="sessions")
    date = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField()
    paid_time = models.DateTimeField(null=True, blank=True)
