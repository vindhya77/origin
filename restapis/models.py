from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.name


class Component(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Attribute(models.Model):
	value = models.CharField(max_length=100)
	component = models.ForeignKey(Component, on_delete=models.CASCADE)


	def __str__(self):
		return self.value 