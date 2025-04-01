from django.shortcuts import render
from .models import Post, PostAttachments
# Create your views here.
def Post_list(request):
    posts = Post.objects.all()
    for post in posts:
        att=PostAttachments.objects.filter(post_id = post.pk)
        post.att = att
    return render(request, 'posts/post_list.html', {'posts':posts} )

def Post_details(request, pid):
    post = Post.objects.get(pk = pid)
    att = PostAttachments.objects.filter(post_id = pid)
    return render(request, 'posts/details_page.html', {'post':post, 'images':att})
