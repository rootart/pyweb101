from django.test import TestCase
from  django.core.urlresolvers import reverse
from tastypie.test import ResourceTestCase

from profiles.models import LandingHypothesisRegistration


class LangindPageHypothesisTestCase(TestCase):
    def setUp(self):
        self.url = reverse('landing-page')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_content_matching(self):
        self.assertIn('Python WEB development course', self.response.content)

    def test_static_matching(self):
        self.assertIn('require-jquery.js', self.response.content)
        self.assertIn('app.css', self.response.content)

    def test_post_request(self):
        response = self.client.post(self.url)
        self.assertEquals(response.status_code, 405)

    def test_context(self):
        self.assertEquals(self.response.context['registered'], 0)


class LandingHypthesisAPITestCase(ResourceTestCase):
    def setUp(self, *args, **kwargs):
        super(LandingHypthesisAPITestCase, self).setUp(*args, **kwargs)
        self.TEST_EMAIL = 'jon.doe@example.com'
        self.post_data = { 
            'email': self.TEST_EMAIL,
            }
        self.LH_ENDPOINT = '/api/langinghypothesis/'

    def test_post_lh_registration(self):
        self.assertEquals(LandingHypothesisRegistration.objects.count(), 0)
        self.assertHttpCreated(self.api_client.post(self.LH_ENDPOINT,
            format='json', data=self.post_data))
        self.assertEqual(LandingHypothesisRegistration.objects.count(), 1)
        self.assertEqual(LandingHypothesisRegistration.objects.all()[0].email,
            self.TEST_EMAIL
            )

    def test_not_allowed_requests(self):
        self.assertHttpMethodNotAllowed(self.api_client.get(self.LH_ENDPOINT))
