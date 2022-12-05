from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Books(models.Model):
    name= models.CharField(max_length=200)
    pages= models.IntegerField()
    price= models.IntegerField()
    author= models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name
