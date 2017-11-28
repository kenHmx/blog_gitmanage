from django.db import models
from django.utils.six import python_2_unicode_compatible

# python_2_unicode_compatible装饰器用于兼容python2
@python_2_unicode_compatible
#创建评论的数据库存储字段
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,blank=True)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    #评论与文章是一对多的映射关系
    post = models.ForeignKey('blog.Post')
    
    def __str__(self):
        return self.text[:20]
  