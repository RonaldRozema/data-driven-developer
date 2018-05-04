from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.views.generic import ListView

from .models import CvEntry
from blog.models import Post


class CvView(ListView):

    model = CvEntry
    template_name = 'cv.html'

    def get_queryset(self):
        result = CvEntry.objects.all().order_by('id')
        if not result:
            return []
        return result[0]

    def get_context_data(self, *args, **kwargs):
        context = super(CvView, self).get_context_data(*args, **kwargs)
        context['popular_post_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).order_by('-times_viewed')[:5]
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context