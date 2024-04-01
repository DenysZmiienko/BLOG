from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

class PostPhoto(models.Model):
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name="Картинка", upload_to="Posts_Photos")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class Tag(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Тегі"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    name = models.CharField(max_length=80, verbose_name="Користувач")
    email = models.EmailField(verbose_name="Пошта")
    body = models.TextField(verbose_name="Коментар")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата зміни")
    # active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

    # def __str__(self):
    #     return self.body

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

class Subscription(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subscriptions', verbose_name="Категорія")
    name = models.CharField(max_length=80, verbose_name="Користувач")
    email = models.EmailField(verbose_name="Пошта")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Підписка"
        verbose_name_plural = "Підписки"

