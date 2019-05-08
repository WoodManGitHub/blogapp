from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=70)
	content = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})
