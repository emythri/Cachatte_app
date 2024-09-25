from django.db import models

# Create your models here.

class Stream(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')  # Or use ForeignKey if applicable

class Subject(models.Model):
    name = models.CharField(max_length=100)
    #stream = models.ForeignKey(Stream, related_name='subjects', on_delete=models.CASCADE)
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional fields you want here
#     name = models.TextField(blank=True)
#     age = models.CharField(max_length=100)
#     # other fields...
    
# # models.py
# from django.contrib.auth.models import User
# from django.db import models

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField(null=True, blank=True)



# class Stream(models.Model):
#     name=models.CharField(max_length=300, null=True)
#     category=models.CharField(max_length=300, null=True)
#     subjects=models.CharField(max_length=300, null=True)
#     # dateofbirth=models.DateTimeField(max_length=300, null=True)
#     def __str__(self):
#         return self.name

# from django.db import models

# class Subject(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Stream(models.Model):
#     name = models.CharField(max_length=100)
#     subjects = models.ManyToManyField(Subject, related_name='streams')

#     def __str__(self):
#         return self.name
# models.py
from django.db import models

class Survey(models.Model):
    QUESTION_1_CHOICES = [
        ('logical learning', 'logical learning'),
        ('analitical learning', 'analitical learning'),
        ('creative learning', 'creative learning'),
    ]
    
    QUESTION_2_CHOICES = [
        ('written exams', 'written exams'),
        ('tests', 'tests'),
        ('puzzeles', 'puzzeles'),
    ]
    
    # QUESTION_3_CHOICES = [
    #     ('logical thinking', 'written exams'),
    #     ('', 'tests'),
    #     ('puzzeles', 'puzzeles'),
    # ]

    # QUESTION_4_CHOICES = [
    #     ('written exams', 'written exams'),
    #     ('tests', 'tests'),
    #     ('puzzeles', 'puzzeles'),
    # ]
    question_1 = models.CharField(max_length=20, choices=QUESTION_1_CHOICES, default='logical learning', name='optimum_learning')
    question_2 = models.CharField(max_length=20, choices=QUESTION_2_CHOICES, default='written exams', name='assesments')

    