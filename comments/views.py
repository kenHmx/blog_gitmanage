from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):

    #先获取被评论的文章，这里使用了Django自带的一个函数，如果文章存在就返回，不存在就返回404页面
    post = get_object_or_404(Post,pk=post_pk)
    
    #http请求有get和post两种，一般用户通过表单提交的数据使用post请求
    #因此下方判断是，只有当用户请求为post时才需要处理表单数据
    
    if request.method=='POST':
        #用户提交的数据存在request.POST中，这是一个类字典对象
        #利用这些数据构造了CommentForm类的实例，这样Djang的表单就生成了
        form = CommentForm(request.POST)
        
        #调用form.is_valid()方法时，django自动检查提交的表单数据是否符合要求
        if form.is_valid():
            #如果数据合法，就调用save()函数保存到数据库
            comment = form.save(commit=False)
            
            #将评论和文章关联起来
            comment.post = post
            
            #将评论存到数据库
            comment.save()
            
            #重定向到文章详情页
            return redirect(post)
            
        else:
            comment_list = post.comment_ste.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'blog/detail.html',context=context)
            
    return redirect(post)
        
        


