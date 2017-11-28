from django import template

from ..models import Post, Category,Tag
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
#通过调用annotate函数统计每个分类下对应的文章数，并在调用filter函数过滤掉数量小于1的
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    

@register.simple_tag  
#调用all函数获取所有的标签 
def get_tags():
    return Tag.objects.all()