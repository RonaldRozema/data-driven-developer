from django.views.generic import ListView

from .models import CvEntry


class CvView(ListView):

    model = CvEntry
    template_name = 'cv.html'