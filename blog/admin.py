from django.contrib import admin
from blog.models import  Author, Post, Tag, Comment

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name','email']

admin.site.register(Author, AuthorAdmin)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ["title"]}

    list_filter = ['date', 'author','tags']
    list_display = ['title','author','date']

admin.site.register(Post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'comment']

admin.site.register(Comment, CommentAdmin)



admin.site.register(Tag)




