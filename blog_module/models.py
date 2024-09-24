from django.db import models
from django.urls import reverse
from account_module.models import User
from django.utils.text import slugify

class ArticleCategory(models.Model):
    title=models.CharField(max_length=127)
    url_title=models.CharField(max_length=127,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    title=models.CharField(max_length=127)
    url_title=models.CharField(max_length=127,unique=True)

    def __str__(self):
        return self.title
    

class Article(models.Model):
    title=models.CharField(max_length=639)
    # image=models.ImageField(upload_to='article_images/%Y/%m/%d') 
    image=models.ImageField(upload_to='article_images/') #development mode
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,editable=False)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    short_description=models.CharField(max_length=511)
    text=models.TextField()
    slug=models.SlugField(unique=True,blank=True,null=True)
    category=models.ManyToManyField(ArticleCategory)
    tags=models.ManyToManyField(ArticleTag,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):

        # if request.user.username:
        #     self.author=request.user.username

        # else:
        #     self.author=request.user.email
        
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})


class ArticleComment(models.Model):
    parent=models.ForeignKey('ArticleComment',on_delete=models.CASCADE,blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE)


class ArticleVisit(models.Model):
    ip=models.CharField(max_length=32)
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} - {self.ip}'