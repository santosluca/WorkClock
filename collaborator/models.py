from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
    
class Collaborator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateTimeField("Data")
    checkin = models.DateTimeField("Hora de entrada")
    checkout = models.DateTimeField("Hora de saída")
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    def __str__(self):
        return self.date
    