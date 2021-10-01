from django.shortcuts import render, HttpResponse,redirect
from .models import Post, BlogComment
from django.contrib import messages
# Create your views here.


def blogHome(request):
    post = Post.objects.all()
    # print(post)
    return render(request, 'blog/blogHome.html', {'posts': post})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    # print(post)
    comments = BlogComment.objects.filter(post=post)
    return render(request, 'blog/blogPost.html', {'post': post, "comments": comments})


def postComment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postsno = request.POST.get("postSno")
        post = Post.objects.get(sno=postsno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'your comment has been submitted successfully !')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,'your Reply has been submitted successfully !')                        
    return redirect(f'/blog/{post.slug}')









# singh               password :- > rajnish
# rajnish              password :> 12345
