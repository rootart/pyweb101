from django.test import TestCase
from django.core.urlresolvers import reverse
from tastypie.test import ResourceTestCase
from tastypie.test import TestApiClient

import datetime
import json

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
        self.assertIn('base.css', self.response.content)

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

    def test_post_lh_extended_registration(self):
        self.post_data = {
            'email': self.TEST_EMAIL,
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '01/01/1991',
            'university': 'KPI',
            'faculty': 'FMF',
            'major': 'math'
        }
        self.assertEquals(LandingHypothesisRegistration.objects.count(), 0)


        # test correct Location header to work with backbone-tastypie
        response = self.api_client.post(self.LH_ENDPOINT, format='json',
            data=self.post_data
        )
        self.assertTrue(response.status_code, 201)
        self.assertTrue(response.has_header('Location'))

        location = response.get('Location')
        entry_response = self.api_client.get(location, format='json')
        entry_data = json.loads(entry_response.content)
        self.assertEqual(entry_data['email'], self.TEST_EMAIL)

        self.assertHttpCreated(response)
        self.assertEqual(LandingHypothesisRegistration.objects.count(), 1)
        entry = LandingHypothesisRegistration.objects.all()[0]
        self.assertEqual(entry.email,
            self.TEST_EMAIL
            )
        self.assertEqual(entry.major, 'math')
        self.assertEqual(entry.first_name, 'John')
        self.assertEqual(entry.date_of_birth, datetime.date(1991, 1, 1))

    def test_throttling(self):
        self.assertEquals(LandingHypothesisRegistration.objects.count(), 0)
        for item in xrange(5):
            data = {
                'email': '%s@gmail.com' % item,
            }
            print item
            self.assertHttpCreated(self.api_client.post(self.LH_ENDPOINT,
                format='json', data=data, **{'REMOTE_ADDR': '192.168.1.1'})
            )
        self.assertEquals(LandingHypothesisRegistration.objects.count(), 5)
        self.assertHttpTooManyRequests(self.api_client.post(self.LH_ENDPOINT,
            format='json', data={'email': '6@gmail.com'}, **{'REMOTE_ADDR': '192.168.1.1'})
        )

    def test_validation(self):
        self.test_post_lh_registration()
        self.assertHttpBadRequest(
            self.api_client.post(self.LH_ENDPOINT,
            format='json', data=self.post_data)
        )
