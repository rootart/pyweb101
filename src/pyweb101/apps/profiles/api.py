from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.throttle import CacheThrottle, CacheDBThrottle
from tastypie.validation import FormValidation

from profiles.models import LandingHypothesisRegistration
from profiles.forms import LHRForm


class LHResource(ModelResource):
    class Meta:
        queryset = LandingHypothesisRegistration.objects.all()
        allowed_methods = ['post',]
        detail_allowed_methods = ['get', ]
        resource_name = 'langinghypothesis'
        serializer = Serializer(formats=['json',])
        authentication = Authentication()
        authorization = Authorization()
        throttle = CacheDBThrottle(
            throttle_at=5, timeframe=60,
            expiration=24*60*60
        )
        always_return_data = True
        detail_uri_name = 'uuid'
        validation = FormValidation(form_class=LHRForm)
            