from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    division = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # Encrypted password storage

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    borrowed_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="borrowed_books", null=True, blank=True)

    def __str__(self):
        return self.title

    # from django.db.models.signals import post_save
    # from django.dispatch import receiver
    #
    # @receiver(post_save, sender=User)
    # def create_student_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Student.objects.create(user=instance)
