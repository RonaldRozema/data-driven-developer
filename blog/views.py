from django.views.generic import ListView
from blog.models import Post


class PostList(ListView):

    template_name='blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('-publish_date')[:5]