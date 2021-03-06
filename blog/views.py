from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models.functions import TruncMonth
from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView

from datetime import date
from functools import reduce

from blog.models import Post, Comment
from blog.forms import CommentForm, SearchForm

import operator


class PostShortList(ListView):

    template_name='blog/shortlist.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-publish_date')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(PostShortList, self).get_context_data(*args, **kwargs)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context

class PostList(ListView):
    
    template_name='blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-publish_date')

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context


class PostDetail(DetailView, FormView):

    template_name = 'blog/details.html'
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        obj = self.get_object()
        obj.times_viewed = obj.times_viewed + 1
        obj.save()
        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comment(content=form.cleaned_data['content'], author=User.objects.get(username='anonymous'), post=post)
        comment.save()
        post.comment_set.add(comment)
        post.save()
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_details', kwargs={'pk': self.get_object().pk})


class ArchiveList(ListView):

    context_object_name = 'post_list'
    template_name = 'blog/archive.html'
    
    def get_queryset(self):
        month = self.kwargs['month']
        year = self.kwargs['year']
        return Post.objects.filter(is_draft=False, is_removed=False, is_public=True, publish_date__year=year, publish_date__month=month).order_by('publish_date')

    def get_context_data(self, *args, **kwargs):
        context = super(ArchiveList, self).get_context_data(*args, **kwargs)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        context['date'] = date(year=self.kwargs['year'], month=self.kwargs['month'], day=1)
        return context

class SearchList(ListView):

    model = Post
    template_name = 'blog/search.html'

    def get_queryset(self):
        search_string = self.request.GET['search']
        if search_string != '':
            return Post.objects.filter(content__icontains=search_string, is_draft=False, is_removed=False, is_public=True)
        return Post.objects.all()
        

    def get_context_data(self, *args, **kwargs):
        context = super(SearchList, self).get_context_data(*args, **kwargs)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['search_result_count'] = self.get_queryset().count();
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context