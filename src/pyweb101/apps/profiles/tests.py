from django.test import TestCase
from  django.core.urlresolvers import reverse


class LangindPageHypothesysTestCase(TestCase):
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
