from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    #objectに対してタイトルを返してあげる。adminで入ってDBの中身を見たときにわかりやすくなる。
    def __str__(self):
        return self.title
    
class Weather(models.Model):
    location = models.CharField(max_length=32)
    weather = models.CharField(max_length=32)
    temperature = models.IntegerField()

    def __str__(self):
        return self.location
    
    #strと似ていて、DBの見やすさ
    class Meta:
        verbose_name = verbose_name_plural = '天気情報'
