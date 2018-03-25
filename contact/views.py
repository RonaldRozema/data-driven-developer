from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm
from .models import ContactFormModel
from blog.models import Post


class ContactFormView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('form_submitted')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ContactFormView, self).get_context_data(*args, **kwargs)
        context['archive_list'] = Post.objects.filter(is_draft=False, is_removed=False, is_public=True).annotate(month=TruncMonth('publish_date')).values('month').annotate(c=Count('id')).values('month', 'c')
        return context