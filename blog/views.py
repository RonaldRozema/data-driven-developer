from django.views.generic import ListView, DetailView
from django.db.models.functions import TruncMonth
from django.db.models import Count
from datetime import date

from blog.models import Post


class PostList(ListView):

    template_name='blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-publish_date')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context


class PostDetail(DetailView):

    template_name = 'blog/details.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        obj = self.get_object()
        obj.times_viewed = obj.times_viewed + 1
        obj.save()
        return context


class ArchiveList(ListView):

    context_object_name = 'post_list'
    template_name = 'blog/archive.html'
    
    def get_queryset(self):
        month = self.kwargs['month']
        year = self.kwargs['year']
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True, publish_date__year=year, publish_date__month=month).order_by('publish_date')

    def get_context_data(self, *args, **kwargs):
        context = super(ArchiveList, self).get_context_data(*args, **kwargs)
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        context['date'] = date(year=self.kwargs['year'], month=self.kwargs['month'], day=1)
        return context