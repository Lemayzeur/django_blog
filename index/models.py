from django.db import models
from django.utils import timezone

class Atik(models.Model):
	jounalis = models.CharField(max_length=100)
	tit = models.CharField(max_length=255)
	kontni = models.TextField(max_length=4000)
	dat_pibliye = models.DateField(default=timezone.now)