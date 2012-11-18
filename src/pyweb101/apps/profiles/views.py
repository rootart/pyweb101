from django.views.generic.base import TemplateView
from profiles.models import LandingHypothesisRegistration


class LandingPageHypothesisView(TemplateView):
     template_name = "profiles/langing-page-hypothesis.html"

     def get_context_data(self, **kwargs):
         context = super(LandingPageHypothesisView, self).get_context_data(**kwargs)
         context['registered'] = LandingHypothesisRegistration.objects.all().count()
         return context
