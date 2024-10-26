from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


# Create your models here.



class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



class Post(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images', null=True)
    slug = models.SlugField(max_length=160,unique=True)
    content = models.TextField(validators=[MinLengthValidator])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    


    def get_absolute_url(self):
        return reverse("single_post", args=[self.slug])
    
    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    username = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True,) # When use ImageField to render image use .url extension!
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return f'{self.comment}'

