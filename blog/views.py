from django.views.generic import ListView, DetailView
from blog.models import Post


class PostList(ListView):

    template_name='blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-publish_date')[:5]


class PostDetail(DetailView):

    template_name = 'blog/details.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        obj = self.get_object()
        obj.times_viewed = obj.times_viewed + 1
        obj.save()
        return context