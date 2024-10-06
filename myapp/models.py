from django.db import models

class bookmodel(models.Model):
    name=models.CharField(max_length=100)
    writter=models.CharField(max_length=100)
    img=models.ImageField(upload_to="Media/book_img")
    published_date=models.DateField()
    type=models.CharField(max_length=100)
