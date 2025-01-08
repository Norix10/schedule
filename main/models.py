from django.db import models

class Lesson(models.Model):
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Понеділок'),
        ('Tuesday', 'Вівторок'),
        ('Wednesday', 'Середа'),
        ('Thursday', 'Четвер'),
        ('Friday', 'П’ятниця'),
        ('Saturday', 'Субота'),
    ])
    time = models.TimeField()
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject} ({self.day_of_week}, {self.time})"


class Teacher(models.Model):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10, default='')
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} "
