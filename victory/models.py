from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    Email_Address = models.EmailField(max_length=100)

    def __str__ (self):
        return self.name
    
class ToDoList(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Text = models.CharField(max_length=300) 

    def __str__ (self):
        return self.Text
