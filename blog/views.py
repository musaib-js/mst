from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .models import BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras
from django.contrib import humanize


def custom_404(request, exception):
    return render(request,'404.html')

def custom_500(request):
    return render(request,'404.html')

def blogHome(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    popularposts = Post.objects.filter()[0:3]
    context = {'allPosts': allPosts, 'popularPosts':popularposts}
    return render(request, 'blog.html', context)

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()

    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blogpost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")

def privacy(request):
    return render(request, 'privacy.html')

def policy(request):
    return render(request, 'policy.html')