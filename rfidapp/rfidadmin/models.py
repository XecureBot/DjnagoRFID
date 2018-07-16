from django.db import models

# Create your models here.

class UserProfile:
    def __init__(self, user_id, tag_id, first_name, last_name, email, role_id, pic_url):
        self.user_id = user_id
        self.tag_id = tag_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role_id = role_id
        self.role_title = 'Trainer' if role_id == 1 else 'Students'
        self.pic_url = pic_url


class Registers(models.Model):
	user_id = models.CharField(max_length=250)
	tag_id  = models.CharField(max_length=250)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.CharField(max_length=150)
	role_id = models.CharField(max_length=250)
	role_title = models.CharField(max_length=250)
	pic_url = models.CharField(max_length=250)
	
	role_title = (student,Trainer)

class MyModel(models.Model):
  color = models.CharField(max_length=6, choices=role_title, default='student')