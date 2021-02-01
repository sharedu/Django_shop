from django.db import models

# Create your models here.
'''
1.模型类需要继承自models.Model
2.系统 会自动为我们添加一个主键id
3.字段
字段名=model.类型（选项）
字段名相当于数据表的字段名
字段名不要使用python mysql等关键字
'''
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)