from django.views.generic import FormView

from core.forms import DownloadForm


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = DownloadForm
    success_url = '.'