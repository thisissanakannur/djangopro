from django.db import models 


class imnps(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    rollno=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name


