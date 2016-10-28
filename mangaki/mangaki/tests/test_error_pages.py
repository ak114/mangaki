from django.test import TestCase, Client

from mangaki.models import Work, Trope


class ErrorPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        Work.objects.create(
            title='Initial D',
            source='Fujiwara Bunta',
            category=anime
        )
        Trope.objects.create(
            trope='INERTIA DORIFTU ?!',
            author='Keisuke Takahashi',
            origin_id='1'
        )

    def test_trope(self):
        response = self.client.get('/404/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(Trope.objects.only('trope').get(pk=1), response.content)
