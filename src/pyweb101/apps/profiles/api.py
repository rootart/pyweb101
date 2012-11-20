from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization

from profiles.models import LandingHypothesisRegistration


class LHResource(ModelResource):
    class Meta:
        queryset = LandingHypothesisRegistration.objects.all()
        allowed_methods = ['post','get']
        resource_name = 'langinghypothesis'
        serializer = Serializer(formats=['json',])
        authentication = Authentication()
        authorization = Authorization()

    def obj_create(self, bundle, request=None, **kwargs):
        super(LHResource, self).obj_create(bundle, request, **kwargs)
            