from django.db import models

# Create your models here.

# Model / table name: Contact
class Contact(models.Model):
	# Contact table fields
	  name 	 = models.CharField(max_length=20)
    email  = models.EmailField(max_length=100)
    phone  = models.IntegerField()
    info 	 = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('feamle', 'Female')
    ))
    image  = models.ImageField(upload_to='images/', blank=True)
    date_added 	= models.DateTimeField(auto_now_add=True)

