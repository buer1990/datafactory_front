from django.db import models

# Create your models here.
from django.utils import timezone
import datetime


# python3 manage.py makemigrations --empty polls 删除已生成的表信息
# python3 manage.py makemigrations 为模型的改变生成迁移文件
# python3 manage.py migrate 来应用数据库迁移

class Tool(models.Model):
    # 每条语句单独执行，不能加逗号，否则会和下句连续执行，哎好久不用脑子都糊涂了额
    """
    数据工具模型
    """
    tool_name = models.CharField(max_length=200)
    create_time = models.DateTimeField('Create time')

    def __str__(self):
        return self.tool_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_time <= now


# 注意ToolAttr再自动创建对象时会被转为toolattr 而非 tool_Attr
class ToolAttr(models.Model):
    """
    数据工具属性模型
    attr_describe 属性描述
    attr_value 属性值
    attr_type 属性类型
    attr_remark
    """
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    attr_describe = models.CharField(max_length=200)
    attr_value = models.CharField(blank=True, max_length=200)
    attr_type_choices = [
        (0, 'text'),
        (1, 'number'),
        (2, 'date'),
        (3, 'tel'),
        (4, 'time'),
        (5, 'datetime'),
        (6, 'email'),
        (7, 'datetime-local'),
    ]
    attr_type = models.IntegerField(choices=attr_type_choices, default=0)
    attr_remark = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.attr_describe

    def __str__(self):
        return self.attr_value


class ToolPath(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    tool_path = models.CharField(max_length=200)

    def __str__(self):
        return self.tool_path
