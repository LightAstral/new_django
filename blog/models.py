from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час")
    text = models.TextField(verbose_name="Коментар")

    def __str__(self):
        return f"{self.author.username} - {self.datetime}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    comments = models.ManyToManyField(Comment, blank=True, verbose_name="Коментарі", related_name='post_comments')
    image = models.ImageField(upload_to='uploads/post', verbose_name="Зображення")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Photo(models.Model):
    image = models.ImageField(upload_to='uploads')
    description = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    comment_count = models.IntegerField(default=0)
    post_count = models.IntegerField(default=0)
    forum_posts = models.IntegerField(default=0)
    blog_posts = models.IntegerField(default=0)
    days_on_site = models.IntegerField(default=0)
    reputation = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
