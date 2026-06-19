from django.db import models

class Student(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Subject(models.Model):

    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Teacher(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.CharField(max_length=255)


    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.last_name