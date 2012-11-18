from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from profiles.models import LandingHypothesisRegistration


class LHResource(ModelResource):
    class Meta:
        queryset = LandingHypothesisRegistration.objects.all()
        allowed_methods = ['post', 'get']
        resource_name = 'langinghypothesis'
        serializer = Serializer(formats=['json',])