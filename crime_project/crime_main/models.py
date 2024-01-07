from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Board(models.Model):
    # 게시글 임시 관련 데이터베이스 모델 정의 (임시저장 기능 포함)
    title =models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='')
    image = models.FileField(upload_to='svg/', default='')
    tag = ArrayField(models.CharField(max_length=100), default=list)
    tag2 = models.CharField(max_length=100, default='')
    # image = models.ImageField(upload_to='images/', null=True, default='')
    def __str__(self):
        return self.title