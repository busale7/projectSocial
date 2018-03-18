from django.db import models
from django.contrib.auth.models import User


class posts(models.Model):
	title =models.CharField(max_length=125)
	author =models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	Details= models.TextField()
	Date_added= models.DateField()
	added_time=models.TimeField()

	def __str__(self):
		return self.title

