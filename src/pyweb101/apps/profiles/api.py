from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.throttle import CacheThrottle, CacheDBThrottle

from profiles.models import LandingHypothesisRegistration


class LHResource(ModelResource):
    class Meta:
        queryset = LandingHypothesisRegistration.objects.all()
        allowed_methods = ['post',]
        resource_name = 'langinghypothesis'
        serializer = Serializer(formats=['json',])
        authentication = Authentication()
        authorization = Authorization()
        throttle = CacheDBThrottle(
            throttle_at=5, timeframe=60,
            expiration=24*60*60
        )

    def obj_create(self, bundle, request=None, **kwargs):
        super(LHResource, self).obj_create(bundle, request, **kwargs)
            