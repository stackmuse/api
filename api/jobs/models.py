from django.db import models

DEGREE = [
    ('None', 'None'),
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('PhD', 'PhD'),
]

EMPLOYMENT = [
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
    ('Contractor', 'Contractor'),
]

WORKPLACE = [
    ('Onsite', 'Onsite'),
    ('Hybrid', 'Hybrid'),
    ('Remote', 'Remote'),
]


class Competency(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Job(models.Model):
    link = models.URLField()
    experience = models.IntegerField()
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, choices=DEGREE, default='None')
    workplace = models.CharField(max_length=255, choices=WORKPLACE, default='Onsite')
    employment = models.CharField(max_length=255, choices=EMPLOYMENT, default='Full-Time')
    competencies = models.ManyToManyField(Competency)

    def __str__(self):
        return f'{self.workplace} {self.role} at {self.company}'
