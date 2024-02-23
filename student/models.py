from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='student/')
    about = models.TextField(null=True, blank=True)
    Category=models.ForeignKey('Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"



class Category(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"