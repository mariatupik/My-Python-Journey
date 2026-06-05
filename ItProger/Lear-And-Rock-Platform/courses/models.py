from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва курсу")
    slug = models.SlugField(unique=True, verbose_name="URL адреса")
    description = models.TextField(verbose_name="Опис курсу", blank=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Зображення курсу")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    video_url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ('course', 'slug')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Коментар від {self.user.username} до '{self.lesson.title}'"