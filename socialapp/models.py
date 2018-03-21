from django.db import models
from django.contrib.auth.models import User 




class Posts(models.Model):
	title =models.CharField(max_length=125)
	author =models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	Details= models.TextField()
	Date_added= models.DateTimeField(auto_now_add=True)
	image= models.ImageField(null=True)
	
	def __str__(self):
		return self.title

class profile(models.Model) :
	avatar = models.ImageField('profile picture', upload_to='static/media/images/avatars/', null=True, blank=True)
	followers= models.ManyToManyField(User, related_name="followers")
	user_name =models.OneToOneField(User ,default=1 , on_delete=models.CASCADE, related_name="user")
	following =models.ManyToManyField(User, related_name="following")

	def __str__(self):
		return str(self.user_name)
	
	
	


class favorit(models.Model): 
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	story =models.ForeignKey(Posts,on_delete=models.CASCADE)
