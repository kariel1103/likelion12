from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from postcrud.models import Post
from .models import Comment

# Create your views here.

def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html', {'form':form, 'post':post})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('postshow', coment_id=comment.pk)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, comment_id):
    post = get_object_or_404(Comment, pk=comment_id)
    post.delete()
    return redirect('list')