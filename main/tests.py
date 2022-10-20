from django.test import TestCase, Client
# Create your tests here.


class TestSomeCase(TestCase):
    def test_my_view(self):
        client = Client()
        response = client.get('/test/')
        self.assertEqual(response.content.decode(), "Привет, коллеги!")
