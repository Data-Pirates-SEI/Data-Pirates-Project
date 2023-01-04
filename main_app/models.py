from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Supply(models.Model):
    name = models.CharField(max_length=50)
    qty = models.PositiveIntegerField(default=0, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplies_detail', kwargs={'pk': self.id})

class Chore(models.Model):
    title=models.CharField(max_length=100)
    creator=models.CharField(max_length=100)
    assignedTo = models.CharField(max_length=100)
    details = models.TextField(max_length=250)
    supplies = models.ManyToManyField(Supply)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"chore_id": self.id})
    
class Comment(models.Model):
    date = models.DateField('comment date')
    author = models.CharField(max_length=100)
    comment = models.TextField(max_length=300, default = 'Enter Comment Here')
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.get_comment_display()} on {self.date}"
    class Meta:
        ordering = ['date']


