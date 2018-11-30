from django.db import models

# Create your models here.
class CityInfo(models.Model):
	city = models.CharField(max_length=200)
	temp_today = models.FloatField(default=10)
	temp_tomorrow = models.FloatField(default=10)
	population = models.PositiveIntegerField()

	def __str__(self):
		return self.city
