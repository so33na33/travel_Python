from django.db import models

# Create your models here.
class place(models.Model):

    image=models.ImageField(upload_to='pictures')
    des=models.TextField()



