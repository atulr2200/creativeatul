from django.db import models
from django.utils.html import format_html



# Create your models here.

# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    #add_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title

class Feedback(models.Model):
    fb_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile =models.CharField( max_length=50)
    feedback = models.TextField(default="")
    #date = models.DateField()
    def __str__(self):
        return self.name

class Language(models.Model):
    lang_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,verbose_name="Title")
    #url = models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(default="")
    def __str__(self):
        return self.title

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,verbose_name="Title")
    #url = models.CharField(max_length=100, null=True, blank=True)
    content= models.TextField(default="")
    image=models.FileField(upload_to='post/')
    file=models.FileField(upload_to='post/')
    amount=models.CharField(max_length=10, default=0)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.title