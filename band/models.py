from django.db import models

class Song(models.Model):
	title = models.CharField(max_length=150)
	released_date = models.DateTimeField(auto_now_add=True)
	song_file = models.FileField(upload_to='songs/')

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	addr = models.TextField(blank=True)
	schedule = models.CharField(max_length=100)
	book_date = models.CharField(max_length=100)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.name


