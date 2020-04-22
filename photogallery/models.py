from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

