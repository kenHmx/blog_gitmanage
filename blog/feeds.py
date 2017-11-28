#使用django中的Feed类实现rss订阅
from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    #显示在用户端rss聚合订阅终端的标题
    title = "欢迎订阅我的博客"
    
    #用户通过rss聚合器跳转到我们网站的目标网站的地址
    link = "r'^rss/$'"
    
    #用户终端显示的一些描述信息
    description = "这是我的个人博客会分享一些自己职场、技术经验"
    
    #需要显示的内容，这里是获取文章列表
    def items(self):
        return Post.objects.all()
     
    #聚合器上显示的内容的标题，也就是文章标题     
    def item_title(self,item):
        return '[%s]%s' %(item.category,item.title)
        
    #聚合去显示内容的描述    
    def item_description(self,item):
        return item.body
        
        
        
        
        