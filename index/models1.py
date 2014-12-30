from urlparse import urlparse

from django.db import models
from django.contrib.auth.models import User

class Solution(models.Model):
	title = models.CharField(max_length=200)
	source = models.TextField(default="")
	points = models.IntegerField(default=1)
	moderator = models.ForeignKey(User, related_name='moderated_solutions')
	voters = models.ManyToManyField(User, related_name='liked_solutions')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title


	class Meta:
		verbose_name_plural = "solutions"
